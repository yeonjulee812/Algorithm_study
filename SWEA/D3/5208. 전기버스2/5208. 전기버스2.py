def f(i, e, c): # i 현재 정류장, e i정류장 도착 시 남은 배터리 용량, c i정류장 이전까지의 교환횟수
    global minV, N
    if e<0: # 에너지 부족
        return
    elif i == N: # 목적지 도착
        if minV > c:
            minV = c
    elif minV == c:
        return
    else:
        f(i+1, bat[i]-1, c+1) # 교환
        f(i+1, e-1, c) # 통과

T = int(input())
for tc in range(1, T+1):
    bat = list(map(int, input().split()))
    N = bat[0]
    minV = 100
    f(2, bat[1]-1, 0)
    print(f'#{tc} {minV}')
