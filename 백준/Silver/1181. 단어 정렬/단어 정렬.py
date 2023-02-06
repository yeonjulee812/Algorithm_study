N = int(input())
import sys
s = {sys.stdin.readline().strip() for _ in range(N)}
print(*sorted(sorted(list(s)), key=lambda x: len(x)), sep='\n')