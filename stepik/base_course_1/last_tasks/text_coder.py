ex_1 = []
ex_1 += input()

ex_2 = []
ex_2 += input()

d = {}
for i in range(len(ex_1)):
    d[ex_1[i]] = ex_2[i]

res_1 = input()
res_11 = ''
res_2 = input()
res_22 = ''

for i in res_1:
    for key, value in d.items():
        if i == key:
            res_11 += value

for i in res_2:
    for key, value in d.items():
        if i == value:
            res_22 += key
print(res_11)
print(res_22)