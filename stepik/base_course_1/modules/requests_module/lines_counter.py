import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.2/316.txt")
s = [i for i in r.text.splitlines()]
print(len(s))