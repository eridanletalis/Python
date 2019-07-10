def is_parent(parent, child, d):
    global flag
    if parent == child:
        flag = True
    if parent in d[child]:
        flag = True
    else:
        for i in d[child]:
            is_parent(parent, i, d)


flag = False
n = int(input())
d = {}
for i in range(n):
    k = input().split()
    if len(k) > 1:
        d[k[0]] = k[2:]
    else:
        d[k[0]] = []

m = int(input())
result = ''
for i in range(m):
    pair = input().split()
    is_parent(pair[0], pair[1], d)
    if flag:
        result += 'Yes\n'
    else:
        result += 'No\n'
    flag = False
print(result)
