def f(i,k,p):
    global maxP
    if i==k:
        if maxP < p:
            maxP = p
            return
    elif maxP >= p:
        return
    for j in range(k):
        if u[j]==0:
            u[j] = 1
            f(i+1,k,p*arr[i][j]/100)
            u[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxP = 0
    u = [0]*N # u[j] 업무가 배정되었는지 표시
    f(0,N,1)
    print(f'#{tc} {maxP*100:.6f}')