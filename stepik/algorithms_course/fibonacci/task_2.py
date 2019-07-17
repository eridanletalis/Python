def fib_digit(n):
    if n <= 2:
        return 1
    else:
        a = 1
        b = 1
        res = 0
        for i in range(3, n + 1):
            res = (a + b) % 10
            a = b
            b = res
        return res


print(fib_digit(317457))


