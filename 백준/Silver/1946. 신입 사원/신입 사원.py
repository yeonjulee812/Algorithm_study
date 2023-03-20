
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = []
    for _ in range(N):
        li.append(tuple(map(int, input().split())))
    li.sort() # 서류전형 기준 오름차순 정렬
    minV = li[0][1]
    cnt = 1 # 시작지점을 포함해서
    for i in range(N): # 면접전형 기준 내림차순에 해당하면 1씩 증가
        t = li[i][1]
        if t < minV: # 즉, minV 갱신될 때마다 카운트
            minV = t
            cnt += 1
    print(cnt)