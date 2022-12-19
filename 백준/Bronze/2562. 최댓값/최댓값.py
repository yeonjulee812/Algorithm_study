list = []
for i in range(1, 10):
    list.append(int(input()))
print(max(list))
print(list.index(max(list))+1)