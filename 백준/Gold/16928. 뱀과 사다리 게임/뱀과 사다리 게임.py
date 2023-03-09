def game():
    queue = [1]
    cnt = 0
    while True:
        s = queue.pop(0)
        if s == 100:
            return visited[s]
        for i in range(1, 7):
            try:
                n = ladder[s+i]
            except:
                n = s+i
            if 1<=n<=100 and not visited[n]:
                queue.append(n)
                visited[n] = visited[s] + 1

N, M = map(int, input().split())
visited = [0]*101
ladder = {}
for _ in range(N+M):
    x, y = map(int, input().split())
    ladder[x] = y
print(game())