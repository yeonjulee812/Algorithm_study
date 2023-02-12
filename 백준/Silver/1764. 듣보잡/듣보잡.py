N, M = map(int, input().split())

unheard = set(input() for _ in range(N))
unseen = set(input() for _ in range(M))

both = unheard.intersection(unseen)
print(len(both), *sorted(list(both)), sep='\n')