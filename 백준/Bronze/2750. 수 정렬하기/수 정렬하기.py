N = int(input())

li = []
for _ in range(N):
    num = int(input())
    li.append(num)

li.sort()

for i in range(N):
    print(li[i])
