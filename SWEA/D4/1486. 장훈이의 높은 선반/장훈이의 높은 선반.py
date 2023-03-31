T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split()) # N 점원 수, B 선반 높이
    h = list(map(int, input().split())) # 점원 키
    bit = [0]*N
    minV = 0
    for i in h:
        minV += i

    for i in range(1<<N): # 부분집합의 수
        sum = 0
        for j in range(N): # bit의 인덱스
            if i&(1<<j):
                bit[j] = 1
                sum += h[j]
        if sum >= B:
            if minV >= sum:
                minV = sum

    print(f'#{tc} {minV-B}')
