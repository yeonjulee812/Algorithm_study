import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 1

while queue:
    ci, cj = queue.popleft()
    for di in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci + di[0], cj + di[1]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and box[ni][nj] != -1:
            queue.append((ni,nj))
            visited[ni][nj] = visited[ci][cj] + 1

ans = -1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and box[i][j] == 0:
            ans = 0
            break
    if ans == 0:
        break
    else:
        if ans < max(visited[i]):
            ans = max(visited[i])

print(ans-1)