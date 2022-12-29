n = int(input())

for i in range(n):
    H, W, N = map(int, input().split())
    if N%H ==0:
        print(str(H)+ str(N//H).zfill(2))
    else:
        print(str(N%H)+str(N//H+1).zfill(2))