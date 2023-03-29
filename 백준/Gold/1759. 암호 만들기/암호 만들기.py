from itertools import combinations
L, C = map(int, input().split())
moeum_list = []
zaeum_list = []
alpha_list = []

for i in input().split():
    if i in 'aeiou':
        moeum_list.append(i)
    else:
        zaeum_list.append(i)

idx = 0
for m in range(1, min(L-1,5)): # 모음의 개수(m) 결정
    for i in list(combinations(moeum_list,m)): # m개의 모음 조합 결정
        for z in list(combinations(zaeum_list,L-m)): # L-m개의 자음 조합 결정
            alpha_list.append([])
            alpha_list[idx] += i
            alpha_list[idx] += z
            idx += 1

print(*sorted(list(''.join(sorted(alpha)) for alpha in alpha_list)), sep='\n')