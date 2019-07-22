def knapsack_without_reps(W, v):
    n = len(v)
    d = [[0] * (n + 1) for i in range(W + 1)]

    for w in range(W + 1):
        d[w][0] = 0
    for i in range(n + 1):
        d[0][i] = 0
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            d[w][i] = d[w][i - 1]
            if v[i - 1] <= w:
                d[w][i] = max(d[w][i], d[w - v[i - 1]][i - 1] + v[i - 1])
    return d[W][n]


def main():
    W, n = [int(i) for i in input().split()]
    v = [int(i) for i in input().split()]
    print(knapsack_without_reps(W, v))


if __name__ == '__main__':
    main()