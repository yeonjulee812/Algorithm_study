N = int(input())
adjL = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adjL[a].append(b)
    adjL[b].append(a)

queue = [1]
while queue:
    v = queue.pop(0)
    for i in adjL[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = v # 자식 인덱스에 부모 번호 입력
print(*visited[2:], sep='\n')



