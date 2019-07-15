def fib_mod(n, m):
        k = 0
        li = [0, 1]
        for i in range(2, n + 1):
            li.append((li[i - 2] + li[i - 1]) % m)
            k += 1
            if (li[i-1] == 0 and li[i] == 1) or k >= 6 * m:
                print(li[i-1], li[i])
                break
        print(li)
        print(k)
        if li[-2] == 0 and li[-1] == 1:
            return li[n % k]
        else:
            return li[n]


print(fib_mod(10, 2))
