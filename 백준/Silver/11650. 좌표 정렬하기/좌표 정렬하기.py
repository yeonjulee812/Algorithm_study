N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    xy = (x, y)
    li.append(xy)
for x, y in sorted(li):
    print(x, y)
