import sys

a = input().split(' ')
n = int(a[0])
m = int(a[1])
result = False

inp = []

for i in range(n):
    arr = list()
    temp = input()
    for j in range(m):
        arr.append(int(temp[j]))
    inp.append(arr)


v = [[0 for i in range(m)]for j in range(n)]
next = [[0, 0, 1]]
cnt = 0
res = 0


def findway(x, y, cnt):
    global result
    v[x][y] = 1
    x = int(x)
    y = int(y)
    if x == n-1 and y == m-1:
        result = True
        return
    d = [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]
    for i in range(4):
        now1 = d[i][0]
        now2 = d[i][1]
        if now1 < 0 or now2 < 0 or now1 >= n or now2 >= m:
            continue
        elif inp[now1][now2] == 1:
            if v[now1][now2] == 0:
                next.append([now1, now2, cnt+1])


while (result != True):
    if len(next) == 0:
        break
    nxt = next.pop(0)

    if v[nxt[0]][nxt[1]] == 1:
        continue
    res = nxt[2]
    findway(nxt[0], nxt[1], res)

print(res)
