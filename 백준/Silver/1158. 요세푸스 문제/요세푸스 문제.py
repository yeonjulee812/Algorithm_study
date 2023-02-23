from collections import deque
p = deque()
N, K = map(int, input().split())
ans = []
for i in range(1, N+1):
    p.append(i)

while p:
    for _ in range(K-1): # K-1번
        p.append(p.popleft())
    ans.append(p[0])
    p.popleft()

ans_str = '<'
for i in ans:
    ans_str += str(i)
    ans_str += ', '
ans_str = ans_str[:-2]
ans_str += '>'
print(ans_str)