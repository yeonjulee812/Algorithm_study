N = input()
li = N.split('-')
li = [i.split('+') for i in li]
temp = []
for i in li:
    s = 0
    for j in i:
        s += int(j)
    temp.append(s)
ans = temp[0]
for i in temp[1:]:
    ans -= i
print(ans)