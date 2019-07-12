def isprime1(n):
    if n == 2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def isprime2(n):
    if n < 6:
        if n == 2:
            return True
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    else:
        for x in range(2, (n // 2) + 1):
            if n % x == 0:
                return False
        return True


def primes(n=2):
    while True:
        if isprime2(n):
            yield n
        n += 1


for i in primes():
    if i < 320000000000000000:
        print(i)
    else:
        break
