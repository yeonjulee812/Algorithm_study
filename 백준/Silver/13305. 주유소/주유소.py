# 처음이면 무조건 주유
# 가격 저렴한거 나올 때마다 주유가격 갱신

N = int(input())
long = list(map(int, input().split()))
price = list(map(int, input().split()))
p = cost = 0

for i in range(N-1):
    if i == 0 or price[i] < price[i+1]:
        p = price[i]
    cost += p*long[i]

print(cost)