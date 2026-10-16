"""Bounded async video adapter. Never resubmits a generation request."""
from pathlib import Path
from urllib.parse import quote,urlparse
from decimal import Decimal
import json,os,time,urllib.request,hashlib
from .toapis_async import ToAPIsClient

def run_video(job):
    model=job['model'];duration=job.get('duration',5);resolution=job.get('resolution','768p')
    if not isinstance(duration,int):raise ValueError('duration must be integer')
    if model=='MiniMax-H3':
        if duration!=5 or resolution!='768p':raise ValueError('This tested preset is H3 5s/768p only')
        body={'model':model,'prompt':job['prompt'],'duration':duration,'resolution':resolution,'aspect_ratio':'1:1'}
        if job.get('image'):body['image_with_roles']=[{'url':job['image'],'role':'first_frame'}]
    elif model=='grok-video-1.5':
        if duration!=4 or resolution!='480p' or not job.get('image'):raise ValueError('This tested preset is Grok first-frame 4s/480p only')
        body={'model':model,'prompt':job['prompt'],'duration':duration,'resolution':resolution,'aspect_ratio':'1:1','video_generation_mode':'first_frame_image_to_video','image':job['image']}
    else:raise ValueError('Uninspected video model')
    client=ToAPIsClient(os.environ.get('TOAPIS_API_KEY'),base=os.environ.get('TOAPIS_BASE_URL','https://toapis.com'))
    rows=client._json('pricing?model='+model);rates=[]
    for item in rows.get('data',[]):
        if item.get('id')!=model:continue
        for rate in item.get('prices',[]):
            c=rate.get('conditions',{});seconds=c.get('duration')
            if str(seconds).removesuffix('s')!=str(duration) or c.get('resolution')!=resolution or rate.get('unit')!='second':continue
            images=c.get('input_image_count',0)
            if images not in (0,1):continue
            cost=Decimal(rate['unit_price'])*duration
            # H3 declares the first five image inputs free. No reference-video/audio inputs in this example.
            if model=='MiniMax-H3' and job.get('image') and int(rate.get('free_input_image_count',0))<1:
                cost+=Decimal(rate.get('input_image_unit_price','0'))
            rates.append(cost)
    if not rates:raise ValueError('No matching duration/resolution rate')
    estimate=max(rates)
    if estimate>Decimal(os.environ.get('TOAPIS_MAX_VIDEO_USD','1')):raise ValueError('Video preset exceeds cap')
    run_id=job['run_id']
    identity=json.dumps({'model':model,'body':body,'run_id':run_id,'origin':client.origin,'key_fingerprint':hashlib.sha256(client.key.encode()).hexdigest()},sort_keys=True)
    file=client.state/(hashlib.sha256(identity.encode()).hexdigest()+'.video.json')
    receipt=json.loads(file.read_text(encoding='utf-8')) if file.exists() else None
    def save():
        temp=file.with_suffix('.tmp');temp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8');os.replace(temp,file)
    if receipt is None:
        receipt={'task_id':None,'state':'submitting','request':body,'catalog_estimate_usd':str(estimate),'billing':None,'observations':[]}
        with file.open('x',encoding='utf-8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
        try:task=client._json('videos/generations',body)
        except Exception:
            receipt['state']='submission_response_uncertain';save();raise RuntimeError('Video submit response uncertain; reconcile task logs, do not retry') from None
        receipt.update(task_id=task.get('id'),state=task.get('status','submitted'));save()
    if not receipt.get('task_id'):raise RuntimeError('No task ID in saved receipt; no repeat POST')
    started=time.monotonic()
    while time.monotonic()-started<900:
        task=client._json('videos/generations/'+quote(receipt['task_id'],safe=''))
        if task.get('model') and task['model']!=model:raise RuntimeError('Task model mismatch')
        receipt.update(state=task.get('status'),billing=task.get('billing'));receipt['observations'].append({'status':task.get('status'),'billing':task.get('billing')});save()
        if task.get('status')=='completed':
            url=task['result']['data'][0]['url'];u=urlparse(url)
            if u.scheme!='https' or u.username or u.password:raise RuntimeError('Unsafe result URL')
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Accept':'video/*'})
            with client.http.open(req,timeout=120) as response:raw=response.read(128*1024*1024+1)
            if len(raw)>128*1024*1024 or b'ftyp' not in raw[:40]:raise RuntimeError('Not a bounded MP4 result')
            receipt['result_url']=url;save()
            return raw,{'task_id':receipt['task_id'],'model':model,'request':{**body,**({'image':'<reference URL omitted>'} if 'image' in body else {}),**({'image_with_roles':[{'url':'<reference URL omitted>','role':'first_frame'}]} if 'image_with_roles' in body else {})},'catalog_estimate_usd':str(estimate),'billing':task.get('billing'),'actual_charge_usd':task.get('billing',{}).get('cost_usd') if isinstance(task.get('billing'),dict) and task['billing'].get('status')=='settled' else None}
        if task.get('status') in ('failed','cancelled','expired'):raise RuntimeError('Video task ended '+str(task.get('status'))+'; no retry')
        time.sleep(8)
    raise RuntimeError('Video pending; resume saved task, never resubmit')
