import sys
input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))
sorted_li = sorted(list(set(li)))

di = {sorted_li[i] : i for i in range(len(sorted_li))}
for i in li:
    print(di[i], end=' ')