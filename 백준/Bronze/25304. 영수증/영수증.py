a = int(input())
b = int(input())
list = []
for i in range(1,b+1):
    A, B = map(int, input().split())
    list.append(A*B)
    
if a==sum(list):
    print('Yes')
else:
    print('No')
    