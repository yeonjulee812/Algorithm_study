import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sorted_li = sorted(list(map(int, input().split())), reverse=True) # 내림차순

li = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = sorted_li[i] + sorted_li[j] + sorted_li[k]
            if sum <= M:
                li.append(sum)
print(max(li))