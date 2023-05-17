import sys

ary = input().split(' ')

def judge(ary):
    copy_ary = list()
    copy_ary = ary
    for i in range(len(ary)):
        index = i
        rindex = len(ary)-1
        start = 0
        end = 0

