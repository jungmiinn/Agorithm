# # 1446 세준이의 등교 지름길
# import heapq
# import sys

# a = list(map(int, input().split(' ')))
# n = a[0]
# d = a[1]
# path = [i for i in range(d+1)]

# arr = list()
# now_d = 0

# for i in range(n):
#     temp = list(map(int, input().split(' ')))
#     if temp[1] <= d:  # 목적지 보다 뒤에 있는거는 걍 안넣음
#         heapq.heappush(arr, (temp[0], temp))

# for i in range(len(arr)):
#     new = heapq.heappop(arr)[1]  # new = [0, 50, 10]
#     # print(new)
#     start = new[0]
#     des = new[1]
#     cost = new[2]
#     if path[des] > cost + path[start]:
#         newend = cost + path[start]
#         for j in range(des+1, d+1):
#             newend += 1
#         # print("newend:", newend)
#         if newend < path[d]:
#            # print(new)
#            path[des] = cost + path[start]
#            for k in range(des+1, d+1):
#                path[k] = path[k-1] + 1
#     newend = 0

# print(path[d])

N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d
print(dis[D])