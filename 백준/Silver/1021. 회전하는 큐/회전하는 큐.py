from collections import deque
N, M = map(int, input().split())
n = deque(i for i in range(1, N+1))
li = list(map(int, input().split()))

leftCnt = rightCnt = 0

for i in li:
    if n.index(i) <= len(n)//2:
        while i != n[0]:
            n.append(n.popleft())
            leftCnt += 1
    else:
        while i != n[0]:
            n.appendleft(n.pop())
            rightCnt += 1
    n.popleft()

print(leftCnt+rightCnt)
