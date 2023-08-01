import heapq
import string

a = list(map(int, input().split(' ')))
n = a[0]
m = a[1]
space = n -1 # 띄어쓰기 공간 수
arr = []

onlyletter = 0 # 총 글자수 몇개인지

for i in range(n):
   st = input()
   temp = [len(st), st]
   onlyletter += temp[0]
   arr.append(st)


needfill = m - onlyletter #채워야하는 공백
qu = needfill//space # 몫
re = needfill%space #나머지
t = arr[0] # 맨 앞 문자는 그냥 가져오기


for idx in range(1, n):
    if arr[idx][0].islower() and re != 0:
        re -= 1
        t += '_' * (qu + 1) + arr[idx]
    elif idx + re == n:
        re -= 1
        t += '_' * (qu + 1) + arr[idx]
    else:
        t += '_' * qu + arr[idx]

print(t)

