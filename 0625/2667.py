n = int(input())
village = [[] for i in range(n)]

for i in range(n):
    list(map(int, input()))

vis = [[0 for i in range(n)]for j in range(n)]
info = []
cnt = 0


def div(x: int, y: int):
    global cnt
    if vis[x][y] == 1:
        return
    vis[x][y] = 1

    cnt = cnt + 1
    village[x][y] = 0
    # print("now, cnt :", x, y, cnt)
    d = [[x-1, y], [x+1, y], [x, y+1], [x, y-1]]
    for i in range(4):
        new1 = d[i][0]
        new2 = d[i][1]
        if new1 < 0 or new2 < 0 or new1 > n-1 or new2 > n-1:
            continue
        elif village[new1][new2] == 1:
            div(new1, new2)


for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            div(i, j)
            info.append(cnt)
            cnt = 0

print(len(info))
for i in range(len(info)):
    res = min(info)
    print(res)
    info.remove(res)
