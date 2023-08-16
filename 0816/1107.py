goal = int(input())
n = int(input())

gap = abs(goal - 100)
arr = list(map(int, str(goal))) # goal 따로 떼서 저장

board = [i for i in range(10)]
errlist = list(map(int, input().split(' '))) # 안되는거 저장
board = list(set(board) - set(errlist)) # 되는거 저장
print(board)

l = len(str(goal))


for i in range(l):
    if arr[i] not in board:
        arr[i] = -1

if gap < l: # +, - 로만 해결 가능
    print(gap)
elif -1 not in arr: # 못치는거 없을때는 그냥 쌩으로 쳐 
    print(l)
else: # 본격적인 문제상황

