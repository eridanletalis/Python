a = input()
begin_mas = []

while a != 'end':
    begin_mas.append([int(i) for i in a.split()])
    a = input()
for i in range(len(begin_mas)):
    for j in range(len(begin_mas[i])):
        print(begin_mas[i][j - 1] + begin_mas[i - 1][j] + begin_mas[i][j + 1 - len(begin_mas[i])] + begin_mas[i + 1 - len(begin_mas)][j], end = " ")
    print()
