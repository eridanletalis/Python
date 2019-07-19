def interv_count_for_points(points, intervals):
    res = []
    k = 0
    for point in points:
        for interval in intervals:
            if point > interval[1]:
                continue
            elif point < interval[0]:
                continue
            elif point == interval[1]:
                k += 1
            else:
                if point >= interval[0]:
                    k += 1
        res.append(k)
        k = 0
    return " ".join(str(k) for k in res)


def main():
    n, m = map(int, input().split())
    intervals = []
    for i in range(n):
        intervals.append([int(i) for i in input().split()])
    points = [int(i) for i in input().split()]
    print(interv_count_for_points(points, intervals))


if __name__ == "__main__":
    main()