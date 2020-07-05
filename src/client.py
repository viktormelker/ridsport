import requests
import os

username = os.environ['RIDSPORT_USERNAME']
password = os.environ['RIDSPORT_PASSWORD']

base_url = 'https://tdb.ridsport.se'


def login():
    params = {
        'utf8': '✓',
        'authenticity_token': 'OIXIaid7lMuIAUSNyCUClcB9vEZfraPN1Hv726VjTC2cMIyPaV8UhAKpXRzJUbhWWK49zsW6fpHSRpbunBGYfw==',
        'email': username,
        'return_to': '',
        'password': password,
        'commit': 'Logga+in',
    }
    url = base_url + '/session'
    response = requests.post(url, data=params)
    write_file('login_response.html', response.text)


def write_file(filename: str, text: str):
    with open(filename, 'w') as html_file:
        html_file.write(text)
