import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def DFS(arr, start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for i in arr[start]:
        if not visited[i]:
            DFS(arr, i)


N, M, R = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    spot, node = map(int, input().strip().split())
    graph[spot].append(node)
    graph[node].append(spot)

for i in range(N+1):
    graph[i].sort()
cnt = 1
visited = [0] *(N+1)
DFS(graph, R)
[print(visited[i]) for i in range(1, N+1)]
