import requests
from bs4 import BeautifulSoup

# the div class i want is 'headlines-li-div'
r = requests.get('http://abcnews.go.com/')

# this gives us a BeautifulSoup object, which reps the HTML doc as a
# nested data structure
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    print link.get('href'), link.text
