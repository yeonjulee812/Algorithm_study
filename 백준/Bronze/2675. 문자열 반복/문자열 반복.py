a = int(input())

for i in range(a):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')
    print()