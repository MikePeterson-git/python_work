import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
spans = soup('span')
print(len(spans))
sum = 0
for span in spans:
    sum = int(span.text) + sum
print(sum)    
        
