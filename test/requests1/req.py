import requests
import json

with open('req_json.json', 'r', encoding='utf-8') as f:
    js = json.load(f)

url = 'https://qa-gateway.fxqifu.net/pangu/elebuys/zeus/form/info/v2/add'

headers = {
    'authority_token': 'buEFPM3YWjSiFhPYjYQJ4rWU7SPKZ6ob-69787716-2-1'
}

rep = requests.post(url, json=js, headers=headers)

print(rep.json())
