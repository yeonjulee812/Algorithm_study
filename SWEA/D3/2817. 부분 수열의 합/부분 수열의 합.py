def dfs(n,sm):
    global ans
    # [3] 가지치기: 더 이상 정답 갱신 가능성 없는 경우
    # 가장 마지막에, 가장 위쪽에
    if K < sm:
        return

    # [1] 종료조건(n에 관련): 반드시 정답처리는 이곳에서만!
    if n==N:
        if sm == K:
            ans += 1
        return

    # [2] 하부호출
    dfs(n+1, sm+lst[n]) # 포함
    dfs(n+1, sm)        # 포함 X

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0,0)

    print(f'#{tc} {ans}')