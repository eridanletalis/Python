import sys
import requests
import json

client_id = '79a2ce996587b93cece4'
client_secret = 'd6dc606c543c91a8c6fd5cd862f6f208'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
result = []
for line in sys.stdin:
    line = line.rstrip()
    if line == 'end':
        break
    r = requests.get("https://api.artsy.net/api/artists/" + line, headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    result.append([j['sortable_name'], j['birthday']])

result.sort(key=lambda res: (res[1], res[0]))
with open('out.txt', 'a', encoding='utf-8') as file:
    for i in result:
        file.write(i[0] + '\n')
