import heapq
import string

a = list(map(int, input().split(' ')))
n = a[0]
m = a[1]
space = n -1 # 띄어쓰기 공간 수
arr = []
order = []

onlyletter = 0 # 총 글자수 몇개인지

for i in range(n):
   st = input()
   temp = [len(st), st]
   onlyletter += temp[0]
   arr.append(temp)

needfill = m - onlyletter #채워야하는 공백
qu = needfill//space # 몫
re = needfill%space #나머지

underline = "_"*qu # 디폴트 밑줄
flagarr = [] # 추가적으로 넣어줄 밑줄
t = arr[0][1] # 맨 앞 문자는 그냥 가져오기

for i in range(1, n): # 두번째 부터 끝까지 돌면서 _ 보다 순위 낮은애들 고르고 re만큼만 더 있으면 되니까 re 길이될때 까지 밑 줄 추가 인덱스 가져오기
   if ord(arr[i][1][0]) > 95 and len(flagarr)< re:
      flagarr.append(i)

if len(flagarr) == 0 and re != 0: # 만약에 다 대문자면 젤 뒤에 넣어줘야하니까 (re있는 경우만)
   for i in range(re):
      flagarr.append(n-i-1)

for i in range(space): # 그리고 ㄱㄱ flagarr 안에 index랑 겹치면 _ 하나 추가해서 출력 아니면 기본 밑줄만 출력
   if i+1 in flagarr:
      t = t + underline + "_" + arr[i+1][1]
   else:
      t = t + underline + arr[i+1][1]

print(t)

