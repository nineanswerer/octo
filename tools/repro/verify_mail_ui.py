"""Independent Windows UI/result checks against a chosen isolated bundle."""
import argparse
import json
import pathlib
import subprocess
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--bundle', required=True)
parser.add_argument('--output', required=True)
parser.add_argument('--host', default='octosense-ws/OctoSense-App-Hub/target/release/card-host.exe')
args = parser.parse_args()
bundle = (ROOT / args.bundle).resolve()
host = (ROOT / args.host).resolve()
output = (ROOT / args.output).resolve()
assert bundle.is_relative_to(ROOT) and output.is_relative_to(ROOT)
assert host.is_relative_to(ROOT) and host.is_file()
output.mkdir(parents=True, exist_ok=True)
data = output / 'data/no-reminder-agent'
port = 11573
base = 'http://127.0.0.1:' + str(port)
results = []
process = None
handles = []

def request(route, **params):
    url = base + route + ('?' + urllib.parse.urlencode(params) if params else '')
    with urllib.request.urlopen(url, timeout=15) as response:
        result = json.load(response)
    if isinstance(result, dict) and result.get('err'):
        raise RuntimeError(str(result['err']))
    return result

def snap():
    return request('/snap')['s']

def widget(name=None, text=None):
    items = [x for x in snap() if (name is None or x.get('i') == name)
             and (text is None or x.get('t') == text)]
    if len(items) != 1:
        raise AssertionError('Expected one widget: ' + str((name, text, len(items))))
    return items[0]

def click(name=None, text=None):
    for delta in (0, 180, 180, 180, -540, -180, -180):
        if delta:
            request('/m', k='scroll', x=300, y=300, dy=delta, wait=1)
        items = [x for x in snap() if (name is None or x.get('i') == name)
                 and (text is None or x.get('t') == text)]
        if len(items) == 1:
            x,y,w,h = items[0]['r']
            request('/click', x=x+w/2, y=y+h/2, wait=1)
            return
    raise AssertionError('Could not scroll to widget: '+str((name,text)))

def enter(name, text):
    click(name=name)
    request('/k', k='press', c='KeyA', ctrl=1, wait=1)
    request('/t', t=text, wait=1)

def status():
    return widget(name='status_label').get('t', '')

def record(name, ok, **details):
    results.append({'case':name, 'passed':bool(ok), **details})
    if not ok:
        raise AssertionError(name + ': ' + str(details))

def launch():
    global process
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
    for suffix in ('stdout', 'stderr'):
        handles.append((output / ('card-host-' + str(len(handles)) + '.' + suffix + '.log')).open('wb'))
    process = subprocess.Popen([str(host),
        '--bundle', str(bundle), '--app-data', str(output / 'data'), '--allow-unsigned', '--remote', str(port)],
        stdout=handles[-2], stderr=handles[-1], startupinfo=info)
    for attempt in range(30):
        if process.poll() is not None:
            raise RuntimeError('Host exited: ' + str(process.returncode))
        try:
            if any(x.get('i') == 'source_input' for x in snap()):
                time.sleep(.4)
                return
        except (OSError, ValueError):
            pass
        time.sleep(.3)
    raise RuntimeError('UI not ready')

def close():
    global process
    if process is not None and process.poll() is None:
        try:
            request('/quit')
            process.wait(timeout=8)
        except (OSError, subprocess.TimeoutExpired):
            process.terminate()  # Only the exact child this test started.
            process.wait(timeout=8)
    process = None

try:
    launch()
    record('empty_start', not (data / 'user-draft.txt').exists(), status=status())
    click(text='整理草稿')
    record('empty_input', not (data / 'user-draft.txt').exists(), status=status())
    enter('source_input', '今天散步时看到一只猫，记一下。')
    click(text='整理草稿')
    record('no_task', '无需行动' in status() and not (data / 'user-draft.txt').exists(), status=status())
    text = '邮件草稿：本周修复了统计界面，新增事项已验证。邮件还没写完。'
    enter('source_input', text)
    click(text='整理草稿')
    generated = widget(name='draft_input').get('t', '')
    record('generate', text in generated and not (data / 'user-draft.txt').exists(), status=status())
    enter('source_input', text + '修改原文。')
    click(text='确认保存')
    record('source_change_blocks_save', not (data / 'user-draft.txt').exists(), status=status())
    enter('source_input', text)
    click(text='整理草稿')
    generated = widget(name='draft_input').get('t', '')
    edited = generated + '\n我会继续完善真实输入流程。'
    enter('draft_input', edited)
    click(text='确认保存')
    saved = (data / 'user-draft.txt').read_text(encoding='utf-8')
    record('save_and_readback', saved == edited and '核验' in status() and '尚未发送' in status(), status=status())
    click(text='确认保存')
    record('idempotent_save', (data / 'user-draft.txt').read_text(encoding='utf-8') == edited)
    with urllib.request.urlopen(base+'/g?raw=1', timeout=20) as response:
        (output / 'saved-draft.png').write_bytes(response.read())
    close()
    launch()
    record('restart_recovery', widget(name='draft_input').get('t') == edited, status=status())
    click(text='取消')
    click(text='确认保存')
    record('cancel_blocks_save', (data / 'user-draft.txt').read_text(encoding='utf-8') == edited, status=status())
    click(text='清除本地数据')
    record('clear_data', not (data / 'user-draft.txt').exists() and not (data / 'draft-state.json').exists(), status=status())
    (data / 'user-draft.txt').mkdir()  # Test-owned empty directory simulates failed write.
    enter('source_input', text)
    click(text='整理草稿')
    click(text='确认保存')
    record('save_failure', '保存失败' in status() and not (data / 'draft-state.json').exists(), status=status())
    close()
    (data / 'user-draft.txt').rmdir()  # Only that exact empty test directory.
    (data / 'user-draft.txt').write_text('unrelated saved content', encoding='utf-8')
    (data / 'draft-state.json').write_text('{"source":"original","draft":"mismatch"}', encoding='utf-8')
    launch()
    click(text='确认保存')
    record('inconsistent_restore_blocked', (data / 'user-draft.txt').read_text(encoding='utf-8') == 'unrelated saved content'
           and '请先整理' in status(), status=status())
    click(text='清除本地数据')
except Exception as error:
    results.append({'case':'exception', 'passed':False, 'error':type(error).__name__+': '+str(error)})
finally:
    close()
    for handle in handles:
        handle.close()
    (output / 'results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(results, ensure_ascii=False, indent=2))
raise SystemExit(0 if results and all(x['passed'] for x in results) else 1)
