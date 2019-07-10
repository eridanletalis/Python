a = int(input())
x = 0
y = 0

for i in range(a):
    com = [i for i in input().split()]
    if com[0] == 'север':
        y += int(com[1])
    if com[0] == 'юг':
        y -= int(com[1])
    if com[0] == 'восток':
        x += int(com[1])
    if com[0] == 'запад':
        x -= int(com[1])
print(x, y)