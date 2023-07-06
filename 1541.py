n = input()
queue = list()
val = 0
integer = ""
temp = 0


def makingint():
    global integer
    num = int(integer)
    # queue.append(num)
    integer = ""
    return num


for i in range(len(n)):
    if n[i] == '-':
        queue.append(makingint())
        while (True):
            if n[i] == '-':
                break
            i = i+1
            val = val + int(n[i])
        if n[i] == '+':
            queue.append(makingint())
            continue
        else:
            integer = integer + n[i]
    else:
        if n[i] == '+':
            temp = makingint() + temp
        else:
            integer = integer+n[i]


makingint()
for x in range(1, len(queue)):
    fi = fi - int(queue[x])
print(fi)
