import sys


origin_ary = input().split('')
copied_ary = origin_ary
blen = int(len(origin_ary))
front = 0
rear = len(origin_ary) - 1
start = 0
finish = 0

def judge(ary):
    ori_ary = ary
    copy_ary = ary.reverse
    idx = 0
    global start
    global finish
    for i in range(blen): # copy배열을위한 반복문
        for j in range(blen): # 비교하는 반복문
           if ori_ary[j] == copy_ary[idx]:
               start = j
               i = start
               break
        idx = idx + 1


    res = -1  # 0은 이미 완성 1은 부분완성 2는 그냥 없음
    if start == 0 & finish == len(ary)-1: # 완성
        res = 0
    elif start > 0 & finish == len(ary)-1: # 부분완성
        res = 1
    elif start == -1: # 그냥없음
        res = 2

    return res

n = judge(origin_ary)
if n == 0 :

elif n == 1:
elif n ==2: