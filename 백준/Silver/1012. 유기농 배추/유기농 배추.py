T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and farm[i][j]:
                stack = [(i, j)]
                while stack:
                    t = stack.pop()
                    visited[t[0]][t[1]] = cnt + 1
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = t[0] + di, t[1] + dj
                        if 0 <= ni < N and 0 <= nj < M and farm[ni][nj] and not visited[ni][nj]:
                            stack.append((ni, nj))
                cnt += 1

    print(cnt)