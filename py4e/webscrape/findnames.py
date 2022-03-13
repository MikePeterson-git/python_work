import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL -')
position = int(input('Link position: '))
repeat = int(input('Repetition count: '))

# Repeat desired times
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1

        # Stop at position
        if count > position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]
print(name)
