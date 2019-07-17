def max_k(n):
    i = 0
    k = 0
    res = []
    while k < n:
        i += 1
        res.append(i)
        k += i
    if k == n:
        return res
    if k > n:
        res.remove(res[k-n-1])
        return res


n = int(input())
result = max_k(n)
print(len(result))
for i in result:
    print(i, end=" ")
