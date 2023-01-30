import sys
N = int(sys.stdin.readline())
li = [int(sys.stdin.readline().strip()) for i in range(N)]

li.sort()
for i in range(N):
    print(li[i])