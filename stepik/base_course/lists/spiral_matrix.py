a = int(input())
m = [[0] * a for i in range(a)]
k, level = 1, 0
m[a // 2][a // 2] = a * a

for j in range(a // 2):
    for i in range(a - level):
        m[j][i + j] = k
        k += 1
    for i in range(j + 1, a - j):
        m[i][-j - 1] = k
        k += 1
    for i in range(j + 1, a - j):
        m[-j - 1][-i - 1] = k
        k += 1
    for i in range(j + 1, a - (j + 1)):
        m[-i - 1][j] = k
        k += 1
    level += 2
for i in m:
    print(*i)
