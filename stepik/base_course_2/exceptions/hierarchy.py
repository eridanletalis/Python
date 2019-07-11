def is_parent(parent, child, d):
    global result
    if parent in d[child]:
        result.append(child)
    else:
        for i in d[child]:
            is_parent(parent, i, d)


n = int(input())
d = {}
for i in range(n):
    k = input().split()
    if len(k) > 1:
        d[k[0]] = k[2:]
    else:
        d[k[0]] = []

m = int(input())
result = []
except_list = []
for i in range(m):
    except_list.append(input())
for i in range(len(except_list)):
    for j in range(len(except_list) - 1, i, -1):
        is_parent(except_list[i], except_list[j], d)
result = list(dict.fromkeys(result))
for i in result:
    print(i)