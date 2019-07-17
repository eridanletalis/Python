# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.


def intersection(intervals):
    interv_list.sort(key=lambda x: x[1])
    res = [intervals[0][1]]
    for interval in interv_list:
        if interval[0] <= res[-1]:
            continue
        else:
            res.append(interval[-1])
    return res


n = int(input())
interv_list = []

for i in range(n):
    interv_list.append([int(j) for j in input().split()])

result = intersection(interv_list)
print(len(result))
for i in result:
    print(i, end=" ")
