C = int(input())
M = int(input())
adjL = [[] for _ in range(C+1)]
visited = [0 for _ in range(C+1)]
stack = [1]
cnt = -1
for _ in range(M):
    V, W = map(int, input().split())
    adjL[V].append(W)
    adjL[W].append(V)

while stack:
    t = stack.pop()
    if not visited[t]:
        cnt += 1
    visited[t] = 1
    for w in adjL[t]:
        if not visited[w]:
            stack.append(w)

print(cnt)