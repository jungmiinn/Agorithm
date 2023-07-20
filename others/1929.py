
ip = input().split(' ')
start = int(ip[0])
finish = int(ip[1])

all_ary = list()

for i in range(start, finish + 1):
    all_ary.append(i)

def div(ary):
    for i in range(len(all_ary)):
        if ary[i] > 1:
            for j in range(2, int(ary[i]**0.5)+1):
                if ary[i] % j == 0: 
                    ary[i] = -1
                    break

        
div(all_ary)
for i in all_ary:
    if i > 1:
        print(i)
