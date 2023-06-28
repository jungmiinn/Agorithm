import sys

blue = 0
white = 0

n = int(input())
sp = [[0, 0, n]] #starting point


paper = []

for i in range(n):
    ary = []
    inp = input().split(" ")
    for j in range(n):
        ary.append(int(inp[j]))
    paper.append(ary)


def judge(n1, n2, l): # n = start point l = length
    c = paper[n1][n2]
    for i in range(l):
        for j in range(l):
            if paper[n1 + i][n2 + j] != c:
                return False
    return True


while len(sp) != 0:
    now = sp.pop(0)
    n1 = now[0]
    n2 = now[1]
    l = now[2]
    # print("now :", now, "n1, n2, l : ", n1, n2, l, "return : ", judge(n1, n2, l), "/n")
    # temp = judge(n1, n2, l)
    if not judge(n1, n2, l):
        l //= 2
        sp.append([n1, n2, l])
        sp.append([n1 + l, n2, l])
        sp.append([n1, n2 + l, l])
        sp.append([n1 + l, n2 + l, l])
    else:
        if paper[n1][n2] == 1 :
            blue += 1
        else:
            white += 1
    

print(white)
print(blue)