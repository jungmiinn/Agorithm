n = int(input())

mtx = [[0]*n for i in range(n)]
newtri = [[0]*n for i in range(n)]

def cal(i, j):
    left = newtri[i][j] + mtx[i+1][j]
    right = newtri[i][j] + mtx[i+1][j+1]
    return [j, left, right]

for i in range(n):
    temp = list(map(int, input().split(' ')))
    for j in range(i+1):
        mtx[i][j] = temp[j]

newtri[0][0] = mtx[0][0]

for i in range(n-1):
    for j in range(i+1):
       temp = cal(i, j)
       for k in range(2):
          if newtri[i+1][temp[0]+k] < temp[k+1]:
              newtri[i+1][temp[0]+k] = temp[k+1]

print(max(newtri[n-1]))

