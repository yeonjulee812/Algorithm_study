move = [(1,0), (0,1), (-1,0), (0,-1)]
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    i = j = 0
    pang = []       # 풍선 팡 값 저장용
    while i<N and j<M:      
        balloon = board[i][j]   # 풍선 팡!
        for di, dj in move:     # 상하 좌우 팡!
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M:
                balloon += board[ni][nj]
        pang.append(balloon)
        if j == M-1:            # 모든 값에 대해 확인
            i += 1
            j = 0
        else:
            j += 1
    print(f'#{test_case} {max(pang)}')