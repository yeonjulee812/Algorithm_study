a = input()

for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in a:
            print(a.index(i), end=' ')
        else:
            print(-1, end=' ')