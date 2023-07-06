import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
ary = list()

for i in range(n):
    a = int(input())
    if a == 0:
        if len(ary) == 0:
            print("%d\n" % 0)
        else:
            print("%d\n" % heapq.heappop(ary))
    else:
        heapq.heappush(ary, a)
