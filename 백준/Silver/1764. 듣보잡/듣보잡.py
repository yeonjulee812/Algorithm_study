N, M = map(int, input().split())

unheard = set()
for i in range(N):
    unheard.add(input())
unseen = set()
for i in range(M):
    unseen.add(input())

both = unheard.intersection(unseen)
print(len(both), *sorted(list(both)) , sep='\n')