s = input()
sub_s = input()
k = 0
for i in range(len(s) - (len(sub_s)-1)):
    if s[i: i + len(sub_s)] == sub_s:
        k += 1
print(k)