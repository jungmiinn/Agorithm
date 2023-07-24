#절댓값 힙

import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

total = int(input())
heap= list()

for i in range(total):
    val = int(input())
    if val == 0:
        if len(heap) == 0:
           print("%d\n" % 0)
        else:
            print("%d\n" % heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(val), val))