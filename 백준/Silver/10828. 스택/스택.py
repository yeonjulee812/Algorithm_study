from sys import stdin
def input():
    return stdin.readline().rstrip()

N = int(input())
stack = [0]*100000
top = -1

for _ in range(N):
    cmd = input()

    if 'push' in cmd:
        top += 1
        stack[top] = cmd.split()[1]

    if cmd == 'top':
        if top > -1:
            print(stack[top])
        else:
            print(-1)

    if cmd == 'size':
        print(top + 1)

    if cmd == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    if cmd == 'pop':
        if top == -1:
            print(-1)
        else:
            top -= 1
            print(stack[top+1])