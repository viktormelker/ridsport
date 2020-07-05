import requests
import os

username = os.environ['RIDSPORT_USERNAME']
password = os.environ['RIDSPORT_PASSWORD']

base_url = 'https://tdb.ridsport.se'


def login():
    params = {
        'utf8': '✓',
        # 'authenticity_token': ''
        'email': username,
        # 'return_to': ''
        'password': password,
        'commit': 'Logga+in',
    }
    url = base_url + '/session'
    response = requests.post(url, data=params)
    breakpoint()
