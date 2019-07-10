a = int(input())
b = int(input())
c = int(input())
d = int(input())

s = ""

for i in range(a - 1, b + 1):
    if i == a - 1:
        s += " \t"
    else:
        s += str(i) + "\t"
    for j in range(c, d + 1):
        if i == a - 1:
            if j != d:
                s += str(j) + "\t"
            else:
                s += str(j) + "\n"
        else:
            if j != d:
                s += str(i * j) + "\t"
            else:
                s += str(i * j) + "\n"
print(s)