N, K = map(int, input().split())
visited = [0]*100001
queue = [N]
visited[N] = 0
while queue: # BFS
    t = queue.pop(0)
    if t == K:
        break
    else:
        if t+1 < 100001 and not visited[t+1]:
            queue.append(t+1)
            visited[t+1] = visited[t] + 1
        if 0 <= t-1 and not visited[t-1]:
            queue.append(t-1)
            visited[t-1] = visited[t] + 1
        if 2*t < 100001 and not visited[2*t]:
            queue.append(2*t)
            visited[2*t] = visited[t] + 1
print(visited[K])