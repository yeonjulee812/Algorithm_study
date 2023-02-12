N, M = map(int, input().split())

s = set(input() for _ in range(N)) # 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없음
test = [input() for _ in range(M)]

cnt = 0
for i in test:
    if i in s:
        cnt += 1

print(cnt)