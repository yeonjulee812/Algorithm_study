
import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    if n == 0 and not heap:
        print(0)
    elif n == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)