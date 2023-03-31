def f(n,sm): # n 월 인덱스, sm 해당 월까지의 총 요금
    global minV
    if minV < sm:
        return
    if n > 11:
        if minV > sm:
            minV = sm
        return

    f(n+1, sm+min(plan[n]*day,mon))
    f(n+3, sm+tri)

T = int(input())
for tc in range(1, T+1):
    day, mon, tri, year = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = year
    f(0,0)
    print(f'#{tc} {minV}')