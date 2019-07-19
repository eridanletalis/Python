def get_len_lbu(a):
    d = [i for i in range(len(a))]
    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    res = 0
    for i in d:
        res = max(res, i)
    return res


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(get_len_lbu(a))


if __name__ == '__main__':
    main()