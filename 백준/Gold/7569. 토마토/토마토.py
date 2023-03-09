import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
queue = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j] == 1:
                queue.append((h,i,j))
                visited[h][i][j] = 1

while queue:
    ch, ci, cj = queue.popleft()
    for di in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
        nh, ni, nj = ch +di[0], ci + di[1], cj + di[2]
        if 0<=nh<H and 0<=ni<N and 0<=nj<M and not visited[nh][ni][nj] and box[nh][ni][nj] != -1:
            queue.append((nh,ni,nj))
            visited[nh][ni][nj] = visited[ch][ci][cj] + 1

ans = -1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if visited[h][i][j] == 0 and box[h][i][j] == 0:
                ans = 0
                break
        if ans == 0:
            break
        else:
            if ans < max(visited[h][i]):
                ans = max(visited[h][i])

print(ans-1)