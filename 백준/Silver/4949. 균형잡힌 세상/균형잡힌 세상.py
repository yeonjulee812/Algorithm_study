from sys import stdin
def input():
    return stdin.readline().rstrip()

open_li = ['(', '[']
close_li = [')', ']']

while True:
    s = input()
    stack = [0] * 100
    top = -1
    ans = 'yes'

    if s == '.':
        break

    for x in s:
        if x in open_li: # 여는 괄호 있으면 push
            top += 1
            stack[top] = x
        elif x in close_li: # 닫는 괄호 있으면
            if top > -1 and open_li.index(stack[top]) == close_li.index(x): # 스택에 여는 괄호 있고 괄호 형태도 같으면 pop
                top -= 1
            else: # 스택에 여는 괄호 없거나, 괄호 형태 다르면
                ans = 'no' # 오류
                break
    else: # 문자열 검토 끝
        if top > -1: # 스택에 여는 괄호 남아있으면
            ans = 'no' # 오류
    print(ans)