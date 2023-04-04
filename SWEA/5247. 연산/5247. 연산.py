def bfs(n,m):
    Q = []
    visited = [0]*1000001
    Q.append(n) # 시작점 인큐
    visited[n] = 1 # 방문표시

    while Q:
        v = Q.pop(0) # 디큐
        if v == m:
            return visited[v]
        for w in [v+1, v-1, v*2, v-10]: # v에 대해 연산을 수행한 결과가
            if 0<w<=1000000 and not visited[w]: # 방문하지 않았고, 중간 조건도 만족하면
                Q.append(w) # 인큐
                visited[w] = visited[v] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N,M)-1}')
