N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def check(n, row, col):
    global cnt
    s = sum([sum(r[col:col+n]) for r in arr[row:row+n]])
    if s == n**2:
        cnt += 1
        return
    else:
        n //= 2
        if n !=0:
            check(n, row, col)
            check(n, row+n, col)
            check(n, row, col+n)
            check(n, row+n, col+n)

check(N, 0, 0)
blue = cnt
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            arr[i][j] = 0
        else:
            arr[i][j] = 1

check(N, 0, 0)
white = cnt
print(white)
print(blue)
