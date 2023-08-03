# # 에디터

# import sys
# import string

# text = list(input())
# n = int(input())

# def editor(cmd, op, cur):
#     global text
#     if cmd == 'L':
#         if cur > 0:
#             cur -= 1
#     elif cmd == 'D':
#         if cur < len(text):
#             cur += 1
#     elif cmd == 'B':
#         if cur > 0 and cur <= len(text)+1:
#             del text[cur-1]
#             cur -= 1
#     elif cmd == 'P':
#         if cur >= 0 and cur <= len(text)+1:
#             text.insert(cur, op)
#             cur += 1
#     return cur


# for i in range(n):
#     cur = len(text)
#     temp = list(input().split(' '))
#     if temp[0] == 'P':
#         cur = editor('P', temp[1], cur)
#     else:
#         cur = editor(temp[0], "", cur)



# text = ''.join(text)
# print(text)

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()
           
    else:
        st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))




