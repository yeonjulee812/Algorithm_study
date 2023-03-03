import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
# 연결된 컴퓨터 데이터 만들기
network = [[] for _ in range(N+1)]
for _ in range(M):
    spot, node = map(int, input().strip().split())
    network[spot].append(node)
    network[node].append(spot)

cnt = 0     # 감염 숫자
queue = deque([1])      # 방문 리스트 만들기
visited = [0,1] + [0] * (N-1)   # 이미 방문한 곳 체크
# BFS 시작
while queue:
    i = queue.popleft()
    for j in network[i]:
        if not visited[j]:
            cnt += 1
            visited[j] = 1
            queue.append(j)
print(cnt)