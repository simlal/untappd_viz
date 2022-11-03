import urllib.request
import json
import yaml

# Accessing vars from yaml
with open('env.yaml') as f:
    env = yaml.safe_load(f)
client_id = env['client_id']
client_secret = env['client_secret']
baseURL = env['untappd_v4']