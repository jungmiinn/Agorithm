# 1446 세준이의 등교 지름길
import heapq
import sys

a = list(map(int, input().split(' ')))
n = a[0]
d = a[1]
path = [i for i in range(d+1)]

arr = list()
now_d = 0

for i in range(n):
    temp = list(map(int, input().split(' ')))
    if temp[1] <= d:  # 목적지 보다 뒤에 있는거는 걍 안넣음
        heapq.heappush(arr, (temp[0], temp))

for i in range(len(arr)):
    new = heapq.heappop(arr)[1]  # new = [0, 50, 10]
    # print(new)
    start = new[0]
    des = new[1]
    cost = new[2]
    if path[des] > cost + path[start]:
        path[des] = cost + path[start]
        for j in range(des+1, d+1):
            path[j] = path[j-1] + 1

print(path[d])
