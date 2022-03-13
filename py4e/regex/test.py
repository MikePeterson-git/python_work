import re

hand = open('/Users/Home/Desktop/PY4E/regex/regex_sum_1154867.txt')
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y
sum=0
for z in x:
    sum = sum + int(z)

print(sum)