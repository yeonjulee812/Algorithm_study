T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split()) # start
    ti, tj = map(int, input().split()) # target
    visited = [[0]*N for _ in range(N)]
    queue = [(si,sj)]
    visited[si][sj] = 0

    while queue:
        ci, cj = queue.pop(0) # current
        if (ci,cj) == (ti, tj):
            break
        else:
            for dir in ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)):
                ni, nj = ci + dir[0], cj + dir[1] # new
                if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[ci][cj] + 1

    print(visited[ti][tj])

