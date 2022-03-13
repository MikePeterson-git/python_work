import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')
uh = urllib.request.urlopen(url)
data = uh.read()

myJson = json.loads(data)
comments = (myJson["comments"])
sum = 0
for item in comments:
    sum += int(item['count'])
print('sum: ', sum)