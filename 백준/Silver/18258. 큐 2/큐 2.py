from collections import deque
import sys

N = int(input())
d = deque([])

for _ in range(N):
    str = sys.stdin.readline().strip()
    if 'push' in str:
        d.append(int(str.split()[1]))
    elif str == 'front':
        print(-1) if not d else print(d[0])
    elif str == 'back':
        print(-1) if not d else print(d[-1])
    elif str == 'size':
        print(len(d))
    elif str == 'empty':
        print(1) if not d else print(0)
    elif str == 'pop':
        print(-1) if not d else print(d.popleft())