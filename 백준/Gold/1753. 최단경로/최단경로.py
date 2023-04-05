import sys
import heapq # 최소 힙 -> 가까운 거리에 있는 정점들을 반복해서 뽑아내기 위함
V, E = map(int, input().split()) # 1~V 정점번호, E 간선 수
K = int(input()) # 시작정점 번호
INF = 10*V + 1
arr = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    arr[u].append((v,w)) # v 도착점, w 거리

Q = []
heapq.heappush(Q, (0,K)) # 누적거리, 정점번호
dist = [INF for _ in range(V+1)]
dist[K] = 0 # 자기자신은 0

while Q:
    mid = heapq.heappop(Q) # 가장 가까운 거리에 있는 정점 디큐 -> mid[0] 누적거리, mid[1] 정점번호
    for end in arr[mid[1]]: # 그 정점과 인접한 또다른 정점들에 대해 -> end[0] 인접정점, end[1] 정점간 거리
        if dist[end[0]] > mid[0] + end[1]:
            dist[end[0]] = mid[0] + end[1] # 거리 갱신 # dist[mid[1]]이 아니고 mid[0]임에 주의...
            heapq.heappush(Q, (dist[end[0]], end[0]))

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])