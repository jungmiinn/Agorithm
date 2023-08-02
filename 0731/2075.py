# import sys
# import heapq

# n = int(input())
# table = []

# for i in range(n):
#     temp = list(map(int, input().split(' ')))
#     temp.sort(reverse=True)
#     table.append(temp)

# mx = float('-inf')

# for i in range(n):
#     mx = float('-inf')
#     for j in range(n):
#         if table[j][0] > mx:
#             mx = table[j][0]

#     for column in table:
#         if mx in column:
#             column.remove(mx)
#             break

# print(mx)

import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])