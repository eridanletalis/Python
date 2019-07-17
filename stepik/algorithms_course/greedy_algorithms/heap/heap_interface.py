import heapq

a = []
heapq.heapify(a)
a.reverse()
n = int(input())
for i in range(n):
    action = input().split()
    if action[0] == 'ExtractMax':
        print(-heapq.heappop(a))
    if action[0] == 'Insert':
        heapq.heappush(a, -int(action[1]))