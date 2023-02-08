import sys
input = sys.stdin.readline
M = int(input())

for i in range(M):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == M:
        print(i)
        break

if sum != M:
    print(0)