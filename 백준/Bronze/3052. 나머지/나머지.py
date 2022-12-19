list = []
for i in range(10):
    list.append(int(input()))

list_1 = []
for i in list:
    list_1.append(i%42)

print(len(set(list_1)))