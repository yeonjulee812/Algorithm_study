import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global cnt
    visited[x] = 1
    nxt = pick[x]
    if not visited[nxt]: #다음 노드를 방문하지 않았다면 방문하고
        dfs(nxt)
    else:
        if not done[nxt]: # 사이클이 형성된 경우(visited한 번호인데 팀이 아님)
            w = nxt
            while w != x:
                cnt += 1 # 팀원들을 모두 셈
                w = pick[w]
            cnt += 1 # 자기자신을 셈
    done[x] = 1 # 팀이 아님이 확실시 됨

for _ in range(int(input())):
    N = int(input())
    pick = list(map(lambda x : int(x)-1, input().split()))
    visited = [0]*N
    done = [0]*N # 팀인지 아닌지 그 여부가 확인됐으면 1
    cnt = 0
    for i in range(N):
        if not visited[i]:
            dfs(i)
    print(N-cnt)