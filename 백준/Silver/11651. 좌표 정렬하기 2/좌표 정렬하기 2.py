N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    yx = (y, x)
    li.append(yx)
for y, x in sorted(li):
    print(x, y)