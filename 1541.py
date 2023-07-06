n = input()
queue = list()
val = 0
integer = ""
temp = 0
status = False


def makingint():
    global integer
    num = int(integer)
    integer = ""
    return num


i = 0
while(status == False):
    if n[i] == '-':
        status = True
        break
    elif n[i]=='+':
        temp = temp + makingint()
    else:
        integer = integer+n[i]
    i = i + 1
    if  i == len(n):
        status = True
        break
temp = temp + makingint()
queue.append(temp)
while(i < len(n)):
    i = i+1
    if n[i]=='+':
        temp = temp + makingint()
    elif n[i] =='-':
        temp = temp + makingint()
        queue.append(-1*temp)
    else:
        integer = integer+n[i]


fi = 0
for x in range(len(queue)):
    fi = fi + queue[x]
print(fi)
