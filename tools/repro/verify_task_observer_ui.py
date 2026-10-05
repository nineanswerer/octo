"""Native UI/file tests, explicitly SYNTHETIC mail/model transport; not live AI."""
from pathlib import Path
import shutil

helpers = Path(__file__).with_name('verify_mail_ui.py').read_text(encoding='utf-8')
helpers = helpers[:helpers.index('\ntry:\n    launch()')].replace("x.get('i') == 'source_input'", "x.get('i') == 'status_label'")
exec(helpers)
production = bundle
bundle = output/'test-bundle'
shutil.copytree(production, bundle, dirs_exist_ok=True)
source = (bundle/'main.splash').read_text(encoding='utf-8')
assert source.count('host.request(name, args,') == 1
source = source.replace('host.request(name, args,', 'fixture_request(name, args,').replace('start_timeout(30.0,', 'start_timeout(1.0,').replace('start_timeout(45.0,', 'start_timeout(3.0,')
source = '''// TEST ONLY synthetic transport. No mailbox, credential or model access.
fn fixture_request(name, arguments, callback){
    let fixture = fs.read("fixture.json").parse_json()
    fs.append("fixture-calls.txt", name + "\\n")
    let r = fixture[name]
    if name == "model.complete" && r.is_ok && r.data.output.action == "update" && arguments.input.existing.len() > 0 { r.data.output.record_id = arguments.input.existing[0].id }
    if name == "model.complete" { start_timeout(fixture.delay, || callback(r)) }
    else { start_timeout(0.05, || callback(r)) }
}
''' + source
(bundle/'main.splash').write_text(source, encoding='utf-8')
subprocess.run([str(ROOT/'runtime/host-repro/OctoSense-App-Hub/target/release/hub.exe'), 'stamp', str(bundle)], check=True, capture_output=True)
data.mkdir(parents=True, exist_ok=True)

def fixture(body='今天晚上6点前交稿。', action='create', evidence=None, deadline='今天晚上6点前', message='m1', accounts=None, delay=.1, error=False):
    reply = {'action': action, 'record_id': '', 'title': '交稿' if action != 'ignore' else '', 'deadline_text': deadline if action != 'ignore' else '', 'evidence': body if evidence is None else evidence, 'uncertainty': '相对日期，请核对邮件日期'}
    value = {'delay': delay, 'mail.accounts': {'is_ok': True, 'data': accounts if accounts is not None else [{'id':'account1','address':'me@example.invalid'}]},
             'mail.sync': {'is_ok': True, 'data': {'new':1,'total':1}},
             'mail.list': {'is_ok': True, 'data': {'folder':'INBOX','messages':[{'id':message}]}},
             'mail.message': {'is_ok': True, 'data': {'id':message,'body':body,'sender':'编辑','subject':'稿件','date':'2026-10-03T09:00:00+08:00'}},
             'model.complete': {'is_ok':True,'data':{'output':reply}}}
    if error: value['model.complete']={'is_ok':False,'error':'no_provider: no configured runtime model'}
    (data/'fixture.json').write_text(json.dumps(value,ensure_ascii=False),encoding='utf-8')

def saved(): return json.loads((data/'observer-state.json').read_text(encoding='utf-8'))
def enable(): click(text='启用观察与 AI 分析'); time.sleep(.8)
def stop(): click(text='停用观察'); time.sleep(.2)
def wait_status(fragment):
    for _ in range(30):
        if fragment in status(): return
        time.sleep(.2)
    raise AssertionError((fragment,status()))

try:
    fixture()
    launch()
    record('default_off_no_source_calls', not (data/'fixture-calls.txt').exists())
    enable()
    wait_status('保存')
    record('semantic_result_saved_with_provenance', saved()['records'][0]['deadline_text']=='今天晚上6点前' and saved()['records'][0]['source_key']=='account1/INBOX/m1')
    time.sleep(1.5)
    record('same_message_not_reanalyzed', (data/'fixture-calls.txt').read_text().count('model.complete')==1)
    stop()
    fixture(body='交稿改为明天中午。',action='update',deadline='明天中午',message='m2')
    enable(); wait_status('保存'); stop()
    record('followup_updates_same_record', len(saved()['records'])==1 and saved()['records'][0]['deadline_text']=='明天中午' and len(saved()['processed'])==2)
    fixture(body='别人今天晚上6点前交稿。',action='ignore',message='m3')
    enable(); wait_status('无需记录'); stop()
    record('irrelevant_does_not_create_record',len(saved()['records'])==1 and len(saved()['processed'])==3)
    fixture(evidence='.*',message='m4')
    enable(); wait_status('证据');
    record('invented_evidence_not_saved_or_deduped','account1/INBOX/m4' not in saved()['processed'])
    fixture(deadline='明年',message='m5')
    enable(); wait_status('证据');
    record('invented_deadline_rejected','account1/INBOX/m5' not in saved()['processed'])
    fixture(error=True,message='m6')
    enable(); wait_status('no_provider');
    record('provider_failure_stops_and_preserves_retry', 'account1/INBOX/m6' not in saved()['processed'])
    calls = (data/'fixture-calls.txt').read_text().count('model.complete')
    time.sleep(1.5)
    record('provider_failure_no_automatic_retry',(data/'fixture-calls.txt').read_text().count('model.complete')==calls)
    fixture(message='m7',delay=1.5)
    enable(); stop(); time.sleep(2)
    record('stopped_late_reply_not_saved','account1/INBOX/m7' not in saved()['processed'])
    fixture(message='m8',delay=4)
    enable(); wait_status('超时'); time.sleep(1.5)
    record('timeout_late_reply_not_saved','account1/INBOX/m8' not in saved()['processed'])
    fixture(accounts=[])
    enable(); wait_status('没有已授权');
    record('no_authorized_mailbox_no_analysis','没有已授权' in status())
    fixture(accounts=[{'id':'a','address':'a'},{'id':'b','address':'b'}])
    enable(); wait_status('仅支持');
    record('multiple_accounts_scope_refused','仅支持' in status())
    close(); launch()
    record('restart_restores_record_default_off','明天中午' in widget(name='records_label')['t'] and '未启用' in status())
    with urllib.request.urlopen(base+'/g?raw=1',timeout=15) as response:
        (output/'records.png').write_bytes(response.read())
    statefile=data/'observer-state.json'
    statefile.rename(data/'verified-state-backup.json')
    statefile.mkdir()
    fixture(message='save-failure')
    enable(); wait_status('异常')
    record('storage_failure_stops_without_false_record', '明天中午' in widget(name='records_label')['t'] and statefile.is_dir())
    statefile.rmdir()  # Exact empty directory created by this test only.
    (data/'verified-state-backup.json').rename(statefile)
    close()
    (data/'observer-state.json').write_text('{"schema":1,"records":"bad","processed":[]}',encoding='utf-8')
    fixture(); launch(); enable()
    record('malformed_state_preserved',json.loads((data/'observer-state.json').read_text())['records']=='bad' and '异常' in status())
    (output/'results.json').write_text(json.dumps({'passed':True,'cases':results,'synthetic_transport':True,'real_model_called':False},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'passed':True,'checks':len(results),'synthetic_transport':True}))
finally:
    close()
    for handle in handles: handle.close()
