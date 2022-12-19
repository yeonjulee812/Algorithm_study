a, b = map(int, input().split())
c = input()
list= []

for i in c.split():
    if int(i)<b:
        print(i)