"""Record native 0.5.3 UI; explicitly synthetic mail/model, no private data."""
from pathlib import Path
import hashlib
import shutil
import subprocess
import threading

prefix = Path(__file__).with_name('verify_task_observer_ui.py').read_text(encoding='utf-8').split('\ntry:\n')[0]
prefix = prefix.replace("port = 11573", "port = 11605")
prefix = prefix.replace('r.data.output.action == "update"', '(r.data.output.action == "update" || r.data.output.action == "cancel")')
exec(compile(prefix, str(Path(__file__)), 'exec'))
test_bundle = bundle
source = (bundle/'main.splash').read_text(encoding='utf-8')
source = source.replace('南下 · 无提醒 Agent', '南下 · 0.5.3 合成数据演示')
source = source.replace('散落的承诺，自动收拢；后续的变化，持续跟上。', '测试邮箱与预设模型响应；未连接私人邮箱或在线 AI。')
(bundle/'main.splash').write_text(source, encoding='utf-8')
subprocess.run([str(ROOT/'runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe'),'stamp',str(bundle)],check=True,capture_output=True)
frames = output/'frames'
frames.mkdir(exist_ok=False)
finished = threading.Event()
capture_errors=[]
frame_count=0
def capture():
    global frame_count
    last=None
    while not finished.is_set():
        started=time.monotonic()
        try:
            with urllib.request.urlopen(base+'/g?raw=1',timeout=2) as response: last=response.read()
        except OSError as error: capture_errors.append(str(error))
        if last:
            (frames/('frame-%05d.png'%frame_count)).write_bytes(last)
            frame_count+=1
        finished.wait(max(0,.5-(time.monotonic()-started)))
recorder=threading.Thread(target=capture,daemon=True)
scenes=[]
def scene(name,ok,seconds=15):
    record(name,ok,status=status())
    with urllib.request.urlopen(base+'/g?raw=1',timeout=15) as response: (output/(name+'.png')).write_bytes(response.read())
    scenes.append({'name':name,'frame_start':frame_count,'seconds':seconds,'status':status()})
    print(name,flush=True)
    time.sleep(seconds)
def consent():
    click(text='启用观察与 AI 分析');time.sleep(.3)
    click(text='同意本次云分析并开始');time.sleep(.8)
try:
    bundle=production
    launch();recorder.start()
    scene('01-production-empty', '未启用' in status())
    click(text='启用观察与 AI 分析');time.sleep(.5)
    scene('02-production-missing-service', 'no service answers' in status())
    close()
    bundle=test_bundle
    fixture();launch()
    click(text='启用观察与 AI 分析');time.sleep(.4)
    scene('03-synthetic-consent',not (data/'observer-state.json').exists() or len(saved()['records'])==0)
    click(text='同意本次云分析并开始');wait_status('保存');stop()
    scene('04-synthetic-created',len(saved()['records'])==1 and saved()['records'][0]['deadline_text']=='今天晚上6点前')
    fixture(body='交稿改为明天中午。',action='update',deadline='明天中午',message='m2')
    consent();wait_status('保存');stop()
    scene('05-synthetic-updated',len(saved()['records'])==1 and len(saved()['records'][0]['history'])==1 and saved()['records'][0]['deadline_text']=='明天中午')
    fixture(body='这次交稿取消。',action='cancel',deadline='',message='cancel1')
    consent();wait_status('保存');stop()
    scene('06-synthetic-cancelled',saved()['records'][0]['status']=='cancelled' and len(saved()['records'][0]['history'])==2)
    fixture(error=True,message='failure')
    consent();wait_status('no_provider')
    scene('07-synthetic-model-failure','account1/INBOX/failure' not in saved()['processed'])
    previous=saved();close();launch()
    scene('08-synthetic-restart',saved()==previous and '未启用' in status())
finally:
    finished.set()
    if recorder.is_alive():recorder.join(timeout=5)
    close()
    for handle in handles:handle.close()
    report={'version':'0.5.3','passed':bool(results) and all(x['passed'] for x in results),'cases':results,'scenes':scenes,'frame_count':frame_count,'fps':2,'real_model_called':False,'private_mail_used':False,'synthetic_transport':True,'production_source_sha256':hashlib.sha256((production/'main.splash').read_bytes()).hexdigest(),'capture_errors':len(capture_errors)}
    (output/'recording-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'passed':report['passed'],'frames':frame_count}),flush=True)
