li = [True for i in range(123456*2+1)]

for i in range(2, 2*123456+1):
    if li[i] == True:
        j = 2
        while i*j <= 2*123456:
            li[i*j] = False
            j += 1 

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len(list(filter(bool, li[n+1:2*n+1]))))