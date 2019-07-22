def search(num, d, x, a, max_id):
    for k in range(max_id - 1, -1, -1):
        if d[k] == num and a[k] >= x:
            return k


def get_min_lbu(a, n):
    d = [i for i in range(n)]
    print('created2')
    max_len = 0
    max_len_id = 0
    res = []
    for i in range(n):
        print("iter i = ", i)
        d[i] = 1
        # for j in range(i):
        #     if a[j] >= a[i] and d[j] + 1 > d[i]:
        #         d[i] = d[j] + 1
        #         if d[i] > max_len:
        #             max_len = d[i]
        #             max_len_id = i
    res.append(max_len_id + 1)
    print(res)
    j = max_len_id
    for k in range(max_len - 1, 0, -1):
        res.append(search(k, d, a[max_len_id], a, j) + 1)
        j = res[-1]
    res.reverse()
    return res


def main():
    n = int(input())
    a = [int(i) for i in range(n)]
    print('created')
    res = get_min_lbu(a, n)
    print(len(res))
    print(" ".join(str(i) for i in res))


if __name__ == '__main__':
    main()