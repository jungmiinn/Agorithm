import sys

ip = input.split(' ')
n, k = int(ip[0]), int(ip[1])

def compare(point):
    dis1 = abs(k-(point-1))
    dis2 = abs(k-(point+1))
    dis3 = abs(k-(2*point))
    res = min(dis1, dis2, dis3)
    return res

q = []

front = 0
rear = 0
now = n
distance = 0

while(1):