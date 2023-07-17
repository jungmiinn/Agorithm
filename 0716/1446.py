# 1446 세준이의 등교 지름길
import heapq

a = list(map(int, input().split(' ')))
n = a[0]
d = a[1]
heap = list()
accul = 0

for i in range(n):
    temp = list(map(int, input().split(' ')))
    if temp[1] <= d:
        heapq.heappush(heap, (temp[2], temp))


start = [0, 0, 0]
for i in range(n):
    print(start)
    if start[1] == d:
        break
    cmp = heapq.heappop(heap)[1]
    if start[1] < cmp[0]:
        accul  = accul + cmp[0]-start[1]
    accul += cmp[2]
    start = cmp






        