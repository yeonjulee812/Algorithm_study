import sys
S = set()
M = int(input())
for _ in range(M):
    li = sys.stdin.readline().rstrip().split()
    if li[0] == 'all':
        S = set(range(1, 21))
    elif li[0] == 'empty':
        S = set()
    elif li[0] == 'add' and int(li[1]) not in S:
        S.add(int(li[1]))
    elif li[0] == 'remove' and int(li[1]) in S:
        S.remove(int(li[1]))
    elif li[0] == 'check':
        print(1) if int(li[1]) in S else print(0)
    elif li[0] == 'toggle':
        S.remove(int(li[1])) if int(li[1]) in S else S.add(int(li[1]))