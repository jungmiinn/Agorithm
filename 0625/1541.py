#잃어버린 괄호

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
temp = 0
while(i < len(n)):
    i = i+1
    if i == len(n):
        temp = temp + makingint()
        queue.append(-1*temp)
        break
    elif n[i]=='+':
        temp = temp + makingint()
    elif n[i] =='-':
        temp = temp + makingint()
        queue.append(-1*temp)
        temp = 0
    else:
        integer = integer+n[i]


fi = 0
for x in range(len(queue)):
    fi = fi + queue[x]
print(fi)
