# n번째 큰 수

import sys
import heapq
import math

n = int(input())

table = list()
sq = int(n**0.5)

for i in range(n):
    temp = list(map(int, input().split(' ')))
    if i >= sq:
        table.append(temp)
    temp = []

heap = list()

for i in reversed(range(sq+1)):
    for j in reversed(range(n)):
        heapq.heappush(heap, ((table[i][j])*(-1), table[i][j]))


for i in range(n-1):
    heapq.heappop(heap)

print(heapq.heappop(heap)[1])
