a = input().split(' ')
n = int(a[0])
m = int(a[1])


inp = []

for i in range(n):
    arr = list()
    temp = input()
    for j in range(m):
        arr.append(int(temp[j]))
    inp.append(arr)


v = [[0 for i in range(m)]for j in range(n)]
v[0][0] = 1
next = []
cnt = 0

def findway(x, y):
    global cnt
    cnt = cnt + 1
    x = int(x)
    y = int(y)
    if x == n-1 and y == m-1:
        return cnt
    d = [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]
    for i in range(4):
        now1 = d[i][0]
        now2 = d[i][1]
        if now1 < 0 or now2 < 0 or now1 > n-1 or now2 > m-1:
            continue
        elif inp[now1][now2] == 1:
            if v[now1][now2] == 0:
                v[now1][now2] = 1
                next.append([now1, now2])
    nxt= next.pop(0)
    findway(nxt[0], nxt[1])
    
findway(0,0)
print(cnt-2)
