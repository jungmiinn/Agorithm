import sys

origin_ary = input().split('')
copied_ary = origin_ary
front = 0
rear = len(origin_ary) - 1

def judge(ary):
    ori_ary = ary
    copy_ary = ary
    start = 0
    finish = 0
    for i in range(len(ary)):
        if ori_ary[i] == copy_ary[-i-1]:
            start = i
        