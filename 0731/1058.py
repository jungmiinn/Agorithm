# # 지민이가 궁금한 세계에서 가장 유명한 사람 친구
# import copy

# n = int(input())
# arr = []
# save = [0 for i in range(n)]
# copyarr = []
# cp = 0
# v = []

# def counting(x, y, s):
#    if y != s:
#     v.append(y)
#    idx = x+1
#    for idx in range(idx, n):
#         if arr[idx][y] == 'Y'and idx not in v:
#             counting(y, idx, s)
#         else:
#             continue
    
#    return len(v)
           

# for i in range(n): # 입력
#     temp = list(input())
#     arr.append(temp)

# for i in range(n):
#      for j in range(n):
#         cp = 0
#         v = []
#         if arr[j][i] =='Y':
#            l = counting(i, j, i)
#            print(v)
#            if save[i] < l:
#                 save[i] = l

# print(save)
# print(max(save))

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
# 2-친구 사이일 때 1, 아니면 0
f = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      # 2-친구인 경우
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        f[i][j] = 1

res = 0

for row in f:
  res = max(res,sum(row))
print(res)