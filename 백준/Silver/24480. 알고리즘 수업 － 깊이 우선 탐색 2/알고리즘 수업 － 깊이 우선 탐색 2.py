import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
adjL = [[] for _ in range(N+1)] # 메모리초과 피하기 위해 인접리스트 활용
visited = [0]*(N+1)
stack= [R]
cnt = 1
for _ in range(M): # 인접행렬
    m, n = map(int, input().split())
    adjL[m].append(n)
    adjL[n].append(m)

for i in adjL:
    i.sort()

while stack:
    t = stack.pop()
    if visited[t]:
        continue
    visited[t] = cnt
    cnt += 1
    for w in adjL[t]: # 방문안한 인접점들 push
        if not visited[w]:
            stack.append(w) # pop할 때 오름차순으로 나옴

print(*visited[1:], sep='\n')


