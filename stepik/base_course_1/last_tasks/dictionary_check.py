a = int(input())
d = []
for i in range(a):
    d.append(input().lower())

b = int(input())
text = dict()
result = set()
for i in range(b):
    text[i] = [j for j in input().split()]
for i in text.values():
    for j in i:
        k = j
        if k.lower() not in d:
            result.add(j)
for i in result:
    print(i)