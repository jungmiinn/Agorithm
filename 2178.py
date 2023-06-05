import sys

a = input().split(' ')
n = int(a[0])
m = int(a[1])
ary = list()
l = list()

# 2차원 입력 리스트 완성
for i in range(n):
    temp = input()
    for j in range(m):
        l.append(temp[j])
    ary.append(l)
