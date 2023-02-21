from collections import deque
cards = deque()
def ans(N):
    for i in range(1, N + 1):
        cards.append(i)
    while len(cards)>1:
        cards.popleft()
        cards.append(cards.popleft())
    return cards
X = int(input())
print(*ans(X))