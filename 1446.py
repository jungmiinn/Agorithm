# 1446 세준이의 등교 지름길
import heapq

a = list(map(int, input().split(' ')))
n = a[0]
d = a[1]
heap = list()

for i in range(n):
    temp = list(map(int, input().split(' ')))
    heapq.heappush(heap, (temp[2], temp))

while(True):
    start = heapq.heappop(heap)
    if start[0] == 0:
        