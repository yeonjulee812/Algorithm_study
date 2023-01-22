N = int(input())
numbers = list(map(int, input().split()))

sosu = 0
for num in numbers:
    error = 0
    for i in range(2, num):
        # 1, 자신을 제외한 수로 나누어떨어지면 소수 아님
        if num % i == 0:
            error += 1
    if error == 0:
        sosu += 1
    if num == 1:
        sosu -= 1
print(sosu)