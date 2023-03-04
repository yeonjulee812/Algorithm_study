N = int(input())
mat = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0

# DFS
for i in range(N):
    for j in range(N):
        if not visited[i][j] and mat[i][j]:
            stack = [(i,j)]
            while stack:
                t = stack.pop()
                visited[t[0]][t[1]] = cnt + 1
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = t[0]+di, t[1]+dj
                    if 0<=ni<N and 0<=nj<N and mat[ni][nj] and not visited[ni][nj]:
                        stack.append((ni,nj))
            cnt += 1

print(cnt)
cnt_li = [0]*(cnt+1)
for i in range(N):
    for j in range(N):
        cnt_li[visited[i][j]] += 1

print(*sorted(cnt_li[1:]), sep='\n')