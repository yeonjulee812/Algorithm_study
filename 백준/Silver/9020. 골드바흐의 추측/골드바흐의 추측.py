li = [i for i in range(10001)] # 0 ~ 10000

for i in range(2, 101): # 2 ~ 100
    if li[i] == i:
        j = 2
        while i*j <= 10000:
            li[i*j] = 0
            j += 1

T = int(input())
for _ in range(T):
    n = int(input())
    half = other_half = n//2
    
    while True:
        first_num = li[half]
        second_num = n - first_num
        if first_num != 0 and second_num in li:
            print(first_num, second_num)
            break
        else:
            half -= 1
            other_half += 1