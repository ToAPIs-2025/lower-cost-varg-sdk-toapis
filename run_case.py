"""Run original API asset examples; application UI acceptance is separate."""
from pathlib import Path
import argparse,json,os,base64,hashlib,io
from api.toapis_worker import run
from api.video import run_video

def main():
    p=argparse.ArgumentParser();p.add_argument('--job',required=True);p.add_argument('--live',action='store_true');a=p.parse_args()
    job=json.loads(Path(a.job).read_text(encoding='utf-8'))
    if not a.live:print(json.dumps({'dry_run':True,'job':job}));return
    if not os.environ.get('TOAPIS_API_KEY'):raise SystemExit('Set TOAPIS_API_KEY privately before --live')
    if job['kind']=='image':
        from PIL import Image
        data=run(job);raw=base64.b64decode(data.pop('b64_json'));im=Image.open(io.BytesIO(raw));im.load()
        output=Path(job['output']);output.parent.mkdir(parents=True,exist_ok=True)
        original=output.with_suffix('.original.'+('jpg' if im.format=='JPEG' else 'png'));original.write_bytes(raw);im.save(output,'PNG')
        receipt=data.pop('receipt');data.pop('url',None)
        billing=receipt.get('billing');data.update(actual_dimensions=[im.width,im.height],original_format=im.format,billing=billing,actual_charge_usd=billing.get('cost_usd') if isinstance(billing,dict) and billing.get('status')=='settled' else None,request=receipt['request'],original_output=str(original).replace('\\','/'))
    else:
        raw,data=run_video(job);output=Path(job['output']);output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(raw)
    data.update(date='2026-10-16',status='completed',prompt=job['prompt'],output=str(output).replace('\\','/'),sha256=hashlib.sha256(raw).hexdigest(),validation_scope='Independent API asset adapter example; upstream application UI and native registration not accepted yet')
    evidence=Path(job['evidence']);evidence.parent.mkdir(parents=True,exist_ok=True);evidence.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:data.get(k) for k in ['model','task_id','status','actual_charge_usd','quote_usd','catalog_estimate_usd','actual_dimensions']}))
if __name__=='__main__':main()
