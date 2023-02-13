import sys
input = sys.stdin.readline

K = int(input())
stack = [0]*100000
top = -1

for _ in range(K):
    i = int(input())
    if i != 0:
        top += 1
        stack[top] = i
    else:
        top -= 1

if top == -1:
    print(0)
else:
    print(sum(stack[:top+1]))
