a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

total = a[0]
l = a[1]

b.sort()
flag = b[0]
cnt = 0

for i in range(1, a[0]):
    if abs(flag-b[i])+1 > l:
        cnt += 1
        flag = b[i]
    else:
        continue

print(cnt+1)