x = int(input())
h = int(input())
m = int(input())

h += x // 60 + (m + (x % 60)) // 60
m += x % 60

print(h)
print(m % 60)