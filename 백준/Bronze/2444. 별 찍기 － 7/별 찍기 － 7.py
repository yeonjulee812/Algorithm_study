import sys
N = int(sys.stdin.readline())

for i in range((2*N-1)//2+1):
    print(' '*(N-1-i) + '*'*(2*i+1))
for i in range((2*N-1)//2-1,-1,-1):
    print(' '*(N-1-i) + '*'*(2*i+1))