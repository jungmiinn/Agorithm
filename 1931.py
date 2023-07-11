#회의실 배정

import heapq
import sys


total = int(input())
heap= list()
ans = 1

for i in range(total):
    val = input().split(' ')
    val = list(map(int, val))
    heapq.heappush(heap, (val[1], val))

next = heapq.heappop(heap)[1]
queue = list()
queue.append(next)

for i in range(1, total):
    temp = heapq.heappop(heap)[1]
    if next[1] <= temp[0]:
       next = temp
       queue.append(next)

print(len(queue))
