tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[125*125*9]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    Q = [(0,0)]
    while Q: # bfs
        i, j = Q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
            ni, nj = di+i, dj+j
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + arr[ni][nj]
    print(f'Problem {tc}: {visited[N-1][N-1]}')
    tc += 1