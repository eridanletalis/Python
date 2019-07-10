import requests

url = "699991.txt"
while url[:2] != 'We':
    r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + url)
    url = r.text
with open('out.txt', 'w') as file_writer:
    file_writer.write(url)