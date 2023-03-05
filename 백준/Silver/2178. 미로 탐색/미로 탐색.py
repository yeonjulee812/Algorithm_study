N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = [(0,0)]
visited[0][0] = 1

while queue:
    i,j = queue.pop(0)
    for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and maze[ni][nj]:
            if not visited[ni][nj]:
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

print(visited[N-1][M-1])