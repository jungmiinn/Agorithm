goal = int(input())
n = int(input())

if n:
    errlist = set(input().split()) # 안되는거 저장
    # board = set(set(board) - set(errlist)) # 되는거 저장
else:
    errlist = set()

gap = abs(goal - 100)

for i in range(1000001):
    for num in str(i):
        if num in errlist:
            break
    else:
        gap = min(gap, len(str(i))+abs(i - goal))

print(gap)


