import sys


origin_ary = input().split('')
copied_ary = origin_ary
front = 0
rear = len(origin_ary) - 1
start = -1
finish = 0

def judge(ary):
    ori_ary = ary
    copy_ary = ary.reverse
    global start
    global finish
    for i in range(len(ary)):
        if ori_ary[i] == copy_ary[i]:
            if start == -1:
                start = i
            else:
                finish = i
    res = -1  # 0은 이미 완성 1은 부분완성 2는 그냥 없음
    if start == 0 & finish == len(ary)-1: # 완성
        res = 0
    elif start > 0 & finish == len(ary)-1: # 부분완성
        res = 1
    elif start == -1:
        res = 2

    return res
