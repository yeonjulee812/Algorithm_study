import sys
from collections import deque
T = int(input())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    d = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    ans = rev = 0
    if n == 0:
        d = deque()
    for i in p:
        if i == 'R':
            rev += 1
        else:
            if d:
                d.pop() if rev%2 else d.popleft()
            else:
                print('error')
                ans = 1
                break
    if not ans:
        if rev%2 ==1:
            d.reverse()
        print('[' + ','.join(d) + ']')