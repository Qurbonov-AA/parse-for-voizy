import requests as r
import json
from pprint import pprint


def post_requests():
    with open('texts.json','r',encoding="utf-8") as f:
        voizy = json.load(f)
        return voizy

print(post_requests())
url = 'https://46b01c6596f2.ngrok.io/upload'
infos = post_requests()

for item in infos.values():
    for i in range(len(item['links'])):
        pprint('link-'+item['links'][i]+' title-'+item['names'][i])
        playload = {'title' : item['names'][i], 'url' : item['links'][i]}    
        
        res = r.post(url,data=playload)
        pprint(res.text)
    break
