import requests
import re

data = requests.get(input())

result = []
for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", data.text):
    domain = link[8]
    if domain not in result:
        result.append(domain)

result.sort()

for domain in result:
    print(domain)
