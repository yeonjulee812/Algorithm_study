import sys
input = sys.stdin.readline
M, N = map(int, input().split())
li = [list(input().rstrip()) for _ in range(M)]

minError = 2500
for m in range(M-7):
    for n in range(N-7):
        cnt1 = cnt2 = 0
        for i in range(m, m+8):
            for j in range(n, n+8):
                if (i+j)%2 == (m+n)%2 and li[i][j] == 'B': # 왼쪽 위 꼭지점 기준
                    cnt1 += 1
                if (i+j)%2 == (m+n+1)%2 and li[i][j] == 'W':
                    cnt1 += 1
                if (i+j)%2 == (m+n)%2 and li[i][j] == 'W': # 오른쪽 아래 꼭지점 기준
                    cnt2 += 1
                if (i+j)%2 == (m+n+1)%2 and li[i][j] == 'B':
                    cnt2 += 1
        error1 = 64 - cnt1
        error2 = 64 - cnt2
        if minError > min(error1, error2):
            minError = min(error1, error2)

print(minError)
