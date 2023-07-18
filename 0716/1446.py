# 1446 세준이의 등교 지름길
import heapq
import builtins

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
    else:
        temp = heapq.heappop(heap)[1]

    if temp[1]-temp[0] < temp[3]:
        accul = accul + temp[1]-temp[0]
    else:
        accul += temp[2]
    start = temp

print(accul)
