import sys
sys.setrecursionlimit(100000)


def search(m, n):
    global loc
    loc[m][n] = 0
    s = list()
    d = [[m, n+1], [m, n-1], [m-1, n], [m+1, n]]
    # print(d)
    for b in range(4):
        new_m = d[b][0]
        new_n = d[b][1]
        if new_n < 0 or new_m < 0 or new_m >= w or new_n >= le:
            continue
        elif loc[new_m][new_n] == 1:
            s.append([new_m, new_n])

    for element in s:
        search(element[0], element[1])


c = int(input())
w = 0
le = 0

for i in range(c):
    cnt = 0
    w = 0
    le = 0
    pos = list()

    ip = input().split(' ')
    m, n, k = int(ip[0]), int(ip[1]), int(ip[2])

    w = m
    le = n
    loc = [[0 for i in range(n)]for j in range(m)]

    for j in range(k):
        x, y = input().split()
        x = int(x)
        y = int(y)
        pos.append([x, y])
        loc[int(x)][int(y)] = 1
    for a in range(k):
        if loc[pos[a][0]][pos[a][1]] == 1:
            # print(pos[a][0], pos[a][1], "\n")
            search(pos[a][0], pos[a][1])
            cnt = cnt + 1
    print(cnt)
