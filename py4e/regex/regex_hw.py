import re
hand = open('/Users/Home/Desktop/PY4E/regex/regex_sum_1154867.txt')
x = list()

for line in hand :
    line.rstrip()

    # doesn't work after here:
    y = re.findall('[0-9]+', line)
    num = int(y[0])

    print(num)

    numList.append(num)
    print('Maximum',max(numList))