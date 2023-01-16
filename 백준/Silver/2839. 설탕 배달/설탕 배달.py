N = int(input())

if N%5 ==0: 
    print(N//5)
elif (N%5 ==1) & (N//5 > 1):
    print((N//5)+1)
elif (N%5 ==2) & (N//5 > 1): # 12 17 22 27 32
    print((N//5)+2)
elif N%5 ==3:
    print((N//5)+1)
elif (N%5 ==4) & (N//5 > 1): # 14 24
    print((N//5)+2)
elif N%3 ==0: # 9
    print(N//3)
else:
    print(-1)