# 에디터

import sys
import string

text = list(input())
n = int(input())
cur = len(text)


def editor(cmd, op):
    global cur, text
    if cmd == 'L':
        if cur > 0:
            cur -= 1
    elif cmd == 'D':
        if cur < len(text)-1:
            cur += 1
    elif cmd == 'B':
        if cur > 0:
            text.remove(cur)
            cur -= 1
    elif cmd == 'P':
        text.insert(cur+1, op)
        cur += 1


for i in range(n):
    temp = list(input().split(' '))
    if temp[0] == 'P':
        editor('P', temp[1])
    else:
        editor(temp[0], "")


print(text)
