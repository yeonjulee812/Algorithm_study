from sys import stdin
def input():
    return stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    stack = [0] * 50
    top = -1
    s = input()

    for x in s:
        if x == '(': # 여는 괄호 있으면 push
            top += 1
            stack[top] = x
        else: # 닫는 괄호 있으면
            if top > -1:
                top -= 1 # pop
            else: # 스택 비어있으면
                print('NO') # 에러
                break
    else: # 문자열 탐색 끝
        if top >-1: # 스택이 남았으면
            print('NO') # 에러
        else: # 스택 비었으면
            print('YES') # 정상