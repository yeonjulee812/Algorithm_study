
def DFS(S):
    ans = []
    lis.append(S)
    visited = [0 for _ in range(N + 1)]
    while lis:
        t = lis.pop()
        if not visited[t]:
            ans.append(str(t))
        visited[t] = 1
        for w in adjL[t]:
            if not visited[w]:
                lis.append(w)
    return ' '.join(ans)

def BFS(S):
    ans = []
    lis.append(S)
    visited = [0 for _ in range(N + 1)]
    while lis:
        t = lis.pop(0)
        if not visited[t]:
            ans.append(str(t))
        visited[t] = 1
        for w in adjL[t]:
            if not visited[w]:
                lis.append(w)
    return ' '.join(ans)

N, M, S = map(int, input().split())
adjL = [[] for _ in range(N+1)]
lis = []
for _ in range(M):
    V, W = map(int, input().split())
    adjL[V].append(W)
    adjL[W].append(V)
for i in range(N+1):
    adjL[i].sort(reverse=True)
print(DFS(S))

for i in range(N+1):
    adjL[i].sort()
print(BFS(S))

