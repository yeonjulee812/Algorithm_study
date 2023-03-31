def find(i,sm): # i 현재 인덱스, sm 현재까지의 부분수열의 총합
    global cnt
    if sm > K: # 가지치기
        return
    if sm ==K: # 종료조건
        cnt += 1
        return
    elif i==N: # 종료조건
        return
    find(i+1, sm+A[i]) # 포함
    find(i+1, sm) # 미포함

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N 수열의 길이, K 기준 합
    A = list(map(int, input().split())) # A 수열
    cnt = 0
    find(0,0)
    print(f'#{tc} {cnt}')