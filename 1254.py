import sys


a = input()
origin_ary = list(a)
blen = int(len(origin_ary))
start = -1

def judge(ary):
    ori_ary = ary
    copy_ary = ary[::-1]
    idx = -1
    global start
    global blen
    for i in range(blen): # start 지정
        if ori_ary[i] == copy_ary[0]:
            start = i
            for j in range(blen-i):
                if ori_ary[j+i] != copy_ary[j]:
                    start = -1
                    break
            if start != -1:
                break
                       
                   
    if start == blen -1:
        return 2
    elif start == 0:
        return 0
    else:
        return 1
    
 
n = judge(origin_ary)

if n == 0 : # 이미완성형
    print(blen)
elif n == 1: # 부분완성형
    print(blen + start)
elif n ==2: # 걍 없음
    print(blen * 2 -1)