from heapq import heappush, heappop

a = [5, 4, 3, 2, 1]
h = []
for i in a:
    heappush(h, i)
print(h)
for i in range(len(h)):
    print(h)
    print(heappop(h))

