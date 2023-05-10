import sys
import math

q = []
ip = input().split(' ')
n, k = int(ip[0]), int(ip[1])

if n > 100000 or n < 0:
    exit
if k > 100000 or k < 0:
    exit
        
    

q.append(n)

pos = [0 for i in range(100001)] # 방문처리
pos[n] = 1
front = 0
now = n
sec = 0
cnt = 0

def queue(point):
    global front
    global cnt
    global sec

    new1 = point - 1
    if new1 >=0 and pos[new1] == 0:
        pos[new1] = 1
        q.append(new1)

    new2 = point + 1
    if new2 <= 100_000 and pos[new2] == 0:
        pos[new2] = 1
        q.append(new2)

    new3 = 2*point
    if new3 <= 100_000 and pos[new3] == 0:
        pos[new3] = 1
        q.append(new3)
    cnt = cnt + 3




    

while True:
    now = q[front]
    if k == now:
        # print(math.log(2*cnt+1, 3))
        sec = int(math.floor(math.log(2*cnt+1, 3)))
        print(sec)
        break
    else:
        front = front + 1
        queue(now)

