N = int(input())

if N == 1:
    pass
else:
    for num in range(2, N+1):
        while True:
            if N % num == 0:
                print(num)
                N = N / num
                pass
            else:
                break
