d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, visited, rate):
    global ans
    if len(visited) == move+1:
        ans += rate
        return
    for idx in range(4): # 4방향 다 보면서
        nx, ny = x + d[idx][0], y + d[idx][1]
        if (nx, ny) not in visited: # 방문한 적 없으면
            visited.append((nx, ny)) # 방문하고
            dfs(nx, ny, visited, rate*prob[idx]) # 다음 번 탐색
            visited.pop()

move, E, W, S, N = map(int, input().split())
prob = [E, W, S, N]
ans = 0

dfs(0, 0, [(0, 0)], 1)
print(ans * (0.01 ** move))
