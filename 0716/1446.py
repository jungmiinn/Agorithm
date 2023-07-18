# 1446 세준이의 등교 지름길
import heapq
import sys

a = list(map(int, input().split(' ')))
n = a[0]
d = a[1]
arr = list()
left_d = d

for i in range(n):
    temp = list(map(int, input().split(' ')))
    if temp[1] <= d and temp[2] < temp[1]-temp[0]:
        # print(pri)
        heapq.heappush(arr,(temp[0], tem
                            p))

dis = list()
for i in range(n):

    