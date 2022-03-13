import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')
# if len(url) < 1: break
uh = urllib.request.urlopen(url)
data = uh.read()
# print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum += int(count.text)

print('sum: ', sum)