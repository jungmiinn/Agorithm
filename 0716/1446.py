# 1446 세준이의 등교 지름길
import heapq
import sys

a = list(map(int, input().split(' ')))
n = a[0]
d = a[1]
path = [1 for i in range(d)]
print(path)

arr = list()
now_d = 0

for i in range(n):
    temp = list(map(int, input().split(' ')))
    if temp[1] <= d and temp[2] < temp[1]-temp[0]:
        heapq.heappush(arr, (temp[0], temp))


def gototheSC(start):
    if now_d == d:
        return
    sc = heapq.heappop(arr)
    for i in range(d):
        left_d -= path[i]
