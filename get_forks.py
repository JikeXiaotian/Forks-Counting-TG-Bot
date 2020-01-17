import requests
import json

r = requests.get('https://api.github.com/orgs/fedora-infra/repos')

json_dict = json.loads(r.text)

for item in json_dict:
    print(item['forks'])
