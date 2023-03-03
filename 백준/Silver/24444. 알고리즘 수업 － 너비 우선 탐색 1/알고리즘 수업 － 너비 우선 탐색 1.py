import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    spot, node = map(int, sys.stdin.readline().strip().split())
    graph[spot].append(node)
    graph[node].append(spot)

for i in range(N+1):
    graph[i].sort()

visited = [0] * (N+1)
queue = deque([R])
cnt = 1
visited[R] = cnt
while queue:
    i = queue.popleft()
    for j in graph[i]:
        if not visited[j]:
            cnt += 1
            visited[j] = cnt
            queue.append(j)
print(*visited[1:], sep='\n')

