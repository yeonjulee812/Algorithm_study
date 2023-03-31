def f(n,i,j,d):  # n 이동횟수, i 현재 행, j 현재 열, d 이어붙인 숫자
    if n==7:
        s.add(d)
        return

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):  # 상하좌우
        ni,nj = i+di, j+dj
        if 0<=ni<4 and 0<=nj<4:  # 갈 수 있으면
            f(n+1,ni,nj,d*10+mat[ni][nj])  # 가


T = int(input())
for tc in range(1, T + 1):
    mat = [list(map(int, input().split())) for _ in range(4)]
    s = set()

    for i in range(4):
        for j in range(4):
            f(1,i,j,mat[i][j])

    print(f'#{tc} {len(s)}')