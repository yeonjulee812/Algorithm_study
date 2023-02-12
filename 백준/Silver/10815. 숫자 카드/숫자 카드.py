N = int(input())
cards = set(map(int, input().split()))
M = int(input())
ref = list(map(int, input().split()))

cnt_li = [0]*M

for i in range(M):
    if ref[i] in cards:
        cnt_li[i] += 1 

print(*cnt_li, sep = ' ')