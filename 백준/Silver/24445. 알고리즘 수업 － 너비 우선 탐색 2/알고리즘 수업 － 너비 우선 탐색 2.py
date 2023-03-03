from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [0]*(N+1)
queue= deque()
queue.append(R)
cnt = 1
for _ in range(M):
    m, n = map(int, input().split())
    adjL[m].append(n)
    adjL[n].append(m)

for i in adjL:
    i.sort(reverse=True)

while queue:
    t = queue.popleft()
    if visited[t]:
        continue
    visited[t] = cnt
    cnt += 1
    for w in adjL[t]:
        if not visited[w]:
            queue.append(w)

print(*visited[1:], sep='\n')


