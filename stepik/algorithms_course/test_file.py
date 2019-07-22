def counter(n):
    a = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        minv = a[i - 1] + 1
        if i % 2 == 0:
            minv = min(minv, a[i//2] + 1)
        if i % 3 == 0:
            minv = min(minv, a[i//3] + 1)
        a[i] = minv
    i = n
    res = [n]
    while i > 1:
        if a[i] == a[i - 1] + 1:
            i -= 1
            res.append(i)
            continue
        if i % 2 == 0 and a[i] == a[i//2] + 1:
            i = i // 2
            res.append(i)
            continue
        i = i // 3
        res.append(i)

    res.reverse()
    return str(a[n]) + '\n' + " ".join(str(i) for i in res)


def main():
    n = int(input())
    print(counter(n))


if __name__ == '__main__':
    main()