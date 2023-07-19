# 비슷한 단어

import sys
import string

n = int(input())
inp = list()

for i in range(n):
    temp = input()
    inp.append(temp)

l = len(inp[0])


def findthepair(text1, text2):
    newt = ""
    old = ""
    new = ""
    for i in range(l):
        if text1[i] == text2[i]:
            if text2[i] not in new and text1[i] not in old:
                old += text1[i]
                new += text2[i]

    for i in range(l):
        if text1[i] != text2[i]:
            if text2[i] not in new and text1[i] not in old:
                old += text1[i]
                new += text2[i]
    table = str.maketrans(old, new)
    newt = text1.translate(table)

    if newt == text2:
        return 1
    else:
        return 0


res = 0
for i in range(n):
    for j in range(i+1, n):
        res = res + findthepair(inp[i], inp[j])

print(res)
