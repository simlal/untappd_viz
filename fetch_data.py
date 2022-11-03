import requests
import json
import yaml
# import time

# Accessing vars from yaml
with open('env.yaml') as f:
    env = yaml.safe_load(f)
client_id = env['client_id']
client_secret = env['client_secret']
baseURL = env['apiURL']
brewery_id = env['brewery_id']

def get_brewery_info() :
    endpoint = '/v4/brewery/info/' + str(brewery_id)
    payload = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'BREWERY_ID' : brewery_id
    }
    print('Fetching Brewery info data')
    resp = requests.get(baseURL+endpoint,params=payload)
    try :
        resp_dict = resp.json()
    except :
        print('Response could not be serialized')
    info = json.dumps(resp_dict, indent=4)
    print(info)
endpoint = '/v4/brewery/info/'
payload = {
    'client_id' : client_id,
    'client_secret' : client_secret,
    'BREWERY_ID' : brewery_id
}

get_brewery_info()