n = int(input())
ary = list()


def printMin():
    global ary
    if len(ary) == 0:
        print(0)
    else:
        mi = min(ary)
        idx = ary.index(mi)
        ary.remove(idx)
        print(mi)


for i in range(n):
    x = int(input())
    if x == 0:
        printMin()
    else:
        ary.append(x)
