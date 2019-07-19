def binary_search(num, sorted_list, x, init_list):
    a, b = 0, len(sorted_list) - 1
    while a <= b:
        m = a + (b - a)//2
        if sorted_list[m] == num and init_list[m] >= x:
            return m
        elif sorted_list[m] > num:
            b = m - 1
        elif sorted_list[m] < num:
            a = m + 1
    return -1


def get_min_lbu(a):
    d = [i for i in range(len(a))]
    max_len = 0
    max_len_id = 0
    res = []
    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[j] >= a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                if d[i] > max_len:
                    max_len = d[i]
                    max_len_id = i
    res.append(max_len_id + 1)
    for k in range(max_len - 1, 0, -1):
        res.append(binary_search(k, d, a[max_len_id], a) + 1)
    res.reverse()
    return res


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    res = get_min_lbu(a)
    print(len(res))
    print(" ".join(str(i) for i in res))


if __name__ == '__main__':
    main()