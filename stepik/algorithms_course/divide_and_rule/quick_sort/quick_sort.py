import bisect


def partition(array, a, b):
    x = array[a]
    j = a
    for i in range(a + 1, b):
        if array[i] <= x:
            j += 1
            c = array[i]
            array[i] = array[j]
            array[j] = c
    c = array[a]
    array[a] = array[j]
    array[j] = c
    return j


def quick_sort(array, a=0, b=None):
    if b is None:
        b = len(array)
    while a < b:
        m = partition(array, a, b)
        if (m - 1)-a > b-(m + 1):
            quick_sort(array, m, b)
            b = m
        else:
            quick_sort(array, a, m)
            a = m + 1


def main():
    n, m = map(int, input().split())
    intervals = []
    for i in range(n):
        intervals.append([int(i) for i in input().split()])
    l_limits = [i[0] for i in intervals]
    r_limits = [i[1] for i in intervals]
    quick_sort(l_limits)
    quick_sort(r_limits)

    points = [int(i) for i in input().split()]
    res = []
    for point in points:
        interv_count = bisect.bisect_right(l_limits, point) - bisect.bisect_left(r_limits, point)
        res.append(interv_count)
    print(" ".join(str(i) for i in res))


if __name__ == "__main__":
    main()