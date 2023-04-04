def f(i, k, s): # i 물건 공장 결정, k 물건 개수, s i-1 상품까지의 생산비용
    global minV
    if i==k:
        if minV > s:
            minV = s
    elif minV <= s: # 가지치기
        return
    else:
        for j in range(k):
            if u[j] == 0:
                u[j] = 1
                f(i+1, k, s+cost[i][j])
                u[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    p = [0]*N # p[i] i 상품을 생산하는 공장 인덱스
    u = [0]*N # u[j] j 공장을 이미 사용했으면 1, 아니면 0
    minV = 1500

    f(0, N, 0)
    print(f'#{tc} {minV}')
