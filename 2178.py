a = input().split(' ')
n = int(a[0])
m = int(a[1])
print(n, m)

inp = []

for i in range(n):
    arr = list()
    temp = input()
    for j in range(m):
        arr.append(int(temp[j]))
    inp.append(arr)
print(inp)

v = [[0 for i in range(n)]for j in range(m)]
next = []


def findway(x, y):
    cnt = cnt + 1
    if a == n & b == m:
        return cnt
    d = [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]
    for i in range(4):
        now1 = d[i][0]
        now2 = d[i][1]
        if v[now1][now2] == 0:
            next.append([now1, now2])
    a = next.pop(0)[0]
    b = next.pop(0)[1]
    findway(a, b)


print(findway(0, 0))
