def f(l,i,j,N,K): # l: 현재 포함해서 지나온 칸 수
    global maxV
    v[i][j] = 1 # 방문 표시
    if maxV < l:
        maxV = l # 최댓값 갱신
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0: # 지도 내부
            if h[i][j] > h[ni][nj]: # 이웃칸이 더 낮은 경우
                f(l+1,ni,nj,N,K)
            elif h[i][j] > h[ni][nj] - K: # 아직 등산로가 아닌 지형중에 깎아서 갈 수 있으면
                tmp = h[ni][nj] # 깎기 전 높이
                h[ni][nj] = h[i][j] - 1
                f(l+1,ni,nj,N,0)
                h[ni][nj] = tmp
    v[i][j] = 0 # 유망하지 않으면 되돌아가야 하므로 초기화

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    h = [list(map(int, input().split())) for _ in range(N)]

    # 최대높이 찾기
    maxH = 0
    for i in range(N):
        for j in range(N):
            if maxH < h[i][j]:
                maxH = h[i][j]

    # 가장 긴 등산로 길이찾기
    maxV = 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if h[i][j] == maxH:
                f(1,i,j,N,K)

    print(f'#{tc} {maxV}')