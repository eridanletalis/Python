def counting_sort(a, m=10):
    b = [0] * (m + 1)
    res = [0] * len(a)
    for j in range(len(a)):
        b[a[j]] += 1
    for i in range(2, len(b)):
        b[i] += b[i - 1]
    for j in range(len(a)-1, -1, -1):
        res[b[a[j]] - 1] = a[j]
        b[a[j]] -= 1
    return res


def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(" ".join(str(i) for i in counting_sort(nums)))


if __name__ == '__main__':
    main()