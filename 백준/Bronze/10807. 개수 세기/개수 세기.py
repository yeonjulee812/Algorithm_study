a = int(input())
b = input()
c = input()
cnt = 0

for i in b.split():
    if i == c:
        cnt += 1
    else:
        pass

print(cnt)