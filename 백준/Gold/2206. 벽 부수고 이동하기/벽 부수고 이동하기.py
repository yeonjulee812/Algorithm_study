from collections import deque
N, M = map(int, input().split())
# visited[i][j][0]은 벽 파괴 가능, visited[i][j][1]은 불가능
visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 3차원 행렬
mat = [list(map(int, input())) for _ in range(N)] # 2차원 행렬
visited[0][0][0] = 1
queue = deque()
queue.append((0,0,0))

def bfs():
    while queue:
        i, j, broke = queue.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][broke]
        for dir in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i + dir[0], j + dir[1]
            if 0<=ni<N and 0<=nj<M:
                # 벽이고 깬적 없다면
                if mat[ni][nj] and not broke:
                    visited[ni][nj][1] = visited[i][j][0] + 1 # 깨고
                    queue.append((ni,nj,1)) # 후보지에 추가(broke = 1로 해서)
                # 벽이 아니고 방문 안한 경우
                elif not mat[ni][nj] and not visited[ni][nj][broke]:
                    visited[ni][nj][broke] = visited[i][j][broke] + 1 # 방문체크
                    queue.append((ni,nj,broke)) # 후보지에 추가
    return -1

print(bfs())