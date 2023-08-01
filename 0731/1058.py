# 지민이가 궁금한 세계에서 가장 유명한 사람? "제목 : 친구"
import copy

n = int(input())
arr = []
save = [0 for i in range(n)]
copyarr = []
res = 0


def counting(x, y):
    print("moved to :", x, y)
    global res
    res += 1 # 친구수 ++
    copyarr[x][y] = 'N'
    copyarr[y][x] = 'N' # 서로서로 일단 n처리 
    for i in range(x, n):
        for j in range(y, n): # 받아온 지점부터 탐색 ㄱㄱ
            if copyarr[i][j] == 'Y':
                counting(j, i) # 찾으면 또 ㄱㄱ
    print("finished at:", x, y)
    return res # 리턴
        

for i in range(n): # 입력
    temp = list(input())
    arr.append(temp)


for i in range(n): 
    for j in range(n):
        if arr[j][i] == 'Y': # y찾기
            copyarr = copy.deepcopy(arr) # 재귀함수에서 쓸 함수 복사
            res = 0 # 얘를 어디서 해줘야하지?
            friend = counting(j, i) # 함수 호출
            print("friend count:", friend)
            if save[i] < friend: # 최대 값 저장해야하니까 비교해서 큰놈만 집어넣기
                save[i] = friend

print(max(save)-1)