T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    diff = [0]*N    # 낙차 구하기
    for i in range(N):
        diff[i] += N - i - 1
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                diff[i] -= 1

    maxV = 0    # 낙차 최댓값 구하기
    for i in range(N):
        if maxV < diff[i]:
            maxV = diff[i]

    print(f'#{tc} {maxV}')