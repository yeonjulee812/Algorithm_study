import sys

input = sys.stdin.readline


N, M, V = map(int, input().strip().split())
# 무향 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    spot, node = map(int, input().strip().split())
    graph[spot].append(node)
    graph[node].append(spot)

# for i in range(1, N+1):
#     graph[i].sort()


stack = [V]
queue = [V]
dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)
dfs_visited[V] = 1
res = []
# DFS
while stack:
    dfs = stack.pop()
    dfs_visited[dfs] = 1
    if dfs not in res:
        res.append(dfs)
    graph[dfs].sort(reverse=1)
    for i in graph[dfs]:
        if not dfs_visited[i]:
            stack.append(i)
print(*res)
# BFS
bfs_visited[V] = 1
while queue:
    bfs = queue.pop(0)
    print(bfs, end=' ')
    graph[bfs].sort()
    for i in graph[bfs]:
        if not bfs_visited[i]:
            bfs_visited[i] = 1
            queue.append(i)
print()
