N = int(input())
stack = []
num = 1
ans = []

for i in range(N):
    n = int(input())
    while num <= n:
        stack.append(num)
        ans.append('+')
        num += 1

    if stack[-1] == n:
        stack.pop()
        ans.append('-')

    else:
        print('NO')
        ans = 0
        break

if ans:
    print('\n'.join(ans))