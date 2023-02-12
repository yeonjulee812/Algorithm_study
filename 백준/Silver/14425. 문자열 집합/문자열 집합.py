N, M = map(int, input().split())

s = set()
for _ in range(N):
    s.add(input())

test = []
for _ in range(M):
    test.append(input())

cnt = 0
for i in test:
    if i in s:
        cnt += 1

print(cnt)