s = []
d = {}
with open('in.txt', 'r') as file_reader:
    for line in file_reader:
        for i in line.strip().lower().split(';'):
            s.append(i)
        for i in range(len(s)):
            if i == 0:
                d[s[i]] = []
            else:
                d[s[0]].append(int(s[i]))
        s.clear()
sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
for grades in d.values():
    for i in range(len(grades)):
        sum0 += grades[i]
        if i == 0:
            sum1 += grades[i]
        if i == 1:
            sum2 += grades[i]
        if i == 2:
            sum3 += grades[i]
    print(sum0 / len(grades))
    sum0 = 0
print(str(sum1 / len(d)) + " " + str(sum2 / len(d)) + " " + str(sum3 / len(d)))