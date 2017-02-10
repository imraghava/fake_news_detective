import requests

r = requests.get('https://newsapi.org/v1/sources?language=en', auth=('USER', 'PW'))
