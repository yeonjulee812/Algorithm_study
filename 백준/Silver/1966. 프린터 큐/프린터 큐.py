T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # N 문서개수, M 해당 문서의 순서
    imp = list(map(int, input().split())) # 중요도

    q = []
    for idx, p in enumerate(imp): # 문서번호, 중요도
        q.append((idx, p))

    cnt = 0
    while q:
        if q[0][1] == max(q, key= lambda x: x[1])[1]:
            if q[0][0] == M:
                break
            q.pop(0)
            cnt += 1
        else:
            q.append(q.pop(0))

    print(cnt+1)
