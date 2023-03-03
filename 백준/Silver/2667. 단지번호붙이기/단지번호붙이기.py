import sys
input = sys.stdin.readline


direction = [(-1,0), (0,1), (1,0), (0,-1)]
N = int(input().strip())
arr = [[0] * (N + 2)] + [[0] + list(map(int, input().strip())) + [0] for _ in range(N)] + [[0]*(N+2)]
total_group_num = 0
stack = []
house_group = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j]:
            total_group_num += 1
            stack.append((i, j))
            house_num = 0
            while stack:            # DFS
                w, h = stack.pop()
                if arr[w][h]:
                    house_num += 1          # 집 개수 세기
                    arr[w][h] = 0
                else:
                    continue
                for di, dj in direction:        # 사방 탐색
                    ni = w + di
                    nj = h + dj
                    if arr[ni][nj]:
                        stack.append((ni, nj))
            house_group.append(house_num)       # 총 집의 개수 저장
print(*[total_group_num, *sorted(house_group)], sep='\n')
