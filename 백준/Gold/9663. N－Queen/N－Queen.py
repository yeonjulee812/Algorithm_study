def backtrack(i,N):
    global cnt
    if i==N:
        cnt += 1
        return
    for j in range(N):
        if col[j]==0 and d1[i+j]==0 and d2[i+N-1-j]==0:
            col[j] = 1
            d1[i+j] = 1
            d2[i+N-1-j] = 1
            backtrack(i+1,N)
            col[j] = 0
            d1[i+j] = 0
            d2[i+N-1-j] = 0

N= int(input())
col = [0]*N # 열
d1 = [0]*(N+N-1) # \ 대각선
d2 = [0]*(N+N-1) # / 대각선
cnt = 0
backtrack(0,N)
print(cnt)