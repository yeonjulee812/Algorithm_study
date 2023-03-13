import sys
sys.setrecursionlimit(10**9)

V = int(input())
dist = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(V):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1):
        if i%2: # 홀수번째(정점)
            dist[temp[0]].append([temp[i], temp[i+1]]) # 무향그래프
            dist[temp[i]].append([temp[0], temp[i+1]])

def dfs(i, sum):
    for a, b in dist[i]:
        if not visited[a]:
            visited[a] = sum + b
            dfs(a, sum+b)

dfs(1,0) # 임의의 한 정점인 1에서 가장 먼거리에 있는 정점(start) 찾고
start = visited.index(max(visited))
visited = [0] * (V+1)
visited[start] = 1 # 정점 제외
dfs(start, 0) # 정점으로부터 가장 먼거리에 있는 경로의 거리를 찾는다.
print(max(visited))

