def dijkstra(s,V): # s 출발, V 마지막 정점 번호
    U = [0]*(N+1)
    U[s] = 1 # 방문기록
    for i in range(N+1):
        D[i] = adjM[s][i] # 각 인접점과의 거리

    for _ in range(N): # 각 정점의 비용
        minV = INF
        w = 0
        for i in range(N+1):
            if U[i]==0 and minV > D[i]: # 방문안했고, 거리가 최소인 정점
                w = i # 정점번호 갱신
                minV = D[i] # 거리의 최소합 갱신
        U[w] = 1 # 최소비용 확정
        for v in range(N+1):
            if 0<adjM[w][v]<INF: # w에 인접인 v의 조건
                D[v] = min(D[v], D[w]+adjM[w][v])

INF = 11
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split()) # N 마지막 연결지점 번호, E 도로의 수
    adjM = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(E):
        s,e,w = map(int, input().split()) # s 시작, e 끝 지점, w 거리
        adjM[s][e] = w

    D = [0]*(N+1)
    dijkstra(0,N)
    print(f'#{tc} {D[N]}')
