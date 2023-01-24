import math
m, n = map(int, input().split())

li = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1):
    if li[i] == True:
        j = 2
        while i*j <= n:
            li[i*j] = False
            j += 1

for i in range(m, n+1):
    if li[i]:
        if i != 1:
            print(i)
        