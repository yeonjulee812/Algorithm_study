M = int(input())
N = int(input())

sosu_list = []
for num in range(M, N+1):
    error = 0
    for i in range(2, num):
        if num % i == 0:
            error += 1    
    if error == 0:
        sosu_list.append(num)
    if num == 1:
        sosu_list.remove(1)

if len(sosu_list) == 0:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))