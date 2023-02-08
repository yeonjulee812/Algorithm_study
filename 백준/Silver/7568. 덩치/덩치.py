T = int(input())
li = [list(map(int, input().split())) for _ in range(T)]

answer = []
for i in range(T):
    cnt = 0
    for j in range(T):
        if i != j and li[i][0]< li[j][0] and li[i][1]< li[j][1]:
            cnt += 1
    answer.append(cnt+1)

print(*answer)