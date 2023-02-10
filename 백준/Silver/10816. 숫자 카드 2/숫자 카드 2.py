N = int(input())
cards = list(map(int, input().split()))
M = int(input())
ref = list(map(int, input().split()))
counts = {}

for k in ref:
    counts[k] = 0


for x in cards:
    if x in counts:
        counts[x] += 1

for x in ref:
    print(counts[x], end = ' ')