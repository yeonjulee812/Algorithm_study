import sys
input = sys.stdin.readline

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for test_case in range(int(input())):
    M, N, K = map(int, input().strip().split())
    farm = [[0] * (M+2) for _ in range(N+2)]

    for _ in range(K):
        x, y = map(int, input().strip().split())
        farm[y+1][x+1] = 1

    ww = 0

    for i in range(1,N+1):
        for j in range(1,M+1):
            if farm[i][j]:
                ww += 1
                stack = [(i,j)]
                while stack:
                    w, h = stack.pop()
                    farm[w][h] = 0
                    for di, dj in direction:
                        ni = w + di
                        nj = h + dj
                        if farm[ni][nj]:
                            stack.append((ni, nj))
    print(ww)



