N = int(input())
import sys
li = []
for _ in range(N):
	age, name = map(str, sys.stdin.readline().strip().split())
	combi = (int(age), name)
	li.append(combi)

for age, name in sorted(li, key=lambda x: x[0]):
	print(age, name)