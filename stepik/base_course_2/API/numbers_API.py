import requests
import sys

for line in sys.stdin:
    line = line.rstrip()
    num_url = "http://numbersapi.com/" + line + "/math"
    params = {'json': 'true'}
    res = requests.get(num_url, params=params)
    text = res.json()['found']
    with open('out.txt', 'a') as file:
        if not text:
            file.write('Boring\n')
        else:
            file.write('Interesting\n')

