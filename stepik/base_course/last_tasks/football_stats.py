def getPoints(a, b):
    if a - b == 0:
        return 1
    if a - b > 0:
        return 3
    else:
        return 0


def fill(index, a, b):
    if index == 0:
        return 1
    if index == 1:
        if getPoints(a, b) == 3:
            return 1
        else:
            return 0
    if index == 2:
        if getPoints(a, b) == 1:
            return 1
        else:
            return 0
    if index == 3:
        if getPoints(a, b) == 0:
            return 1
        else:
            return 0
    if index == 4:
        return getPoints(a, b)


a = int(input())
d = dict()
for i in range(a):
    game = [i for i in input().strip().split(';')]
    teams = [game[0], game[2]]
    score = [int(game[1]), int(game[3])]
    for j in range(2):
        if j % 2 == 0:
            if d.get(teams[j]) is None:
                d[teams[j]] = [0] * 5
            for k in range(5):
                d[teams[j]][k] += fill(k, score[0], score[1])
        else:
            if d.get(teams[j]) is None:
                d[teams[j]] = [0] * 5
            for k in range(5):
                d[teams[j]][k] += fill(k, score[1], score[0])
for key, value in d.items():
    result = key + ":"
    for i in value:
        result += str(i) + " "
    print(result)
