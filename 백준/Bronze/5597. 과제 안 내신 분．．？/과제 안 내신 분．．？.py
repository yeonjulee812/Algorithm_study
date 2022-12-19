list = []
for i in range(1,29):
    list.append(int(input()))

r = range(1,31)
list_1 = [*r]
list_2 = []

for i in list_1:
    if i in list:
        pass
    else:
        list_2.append(int(i))
        
print(min(list_2))
print(max(list_2))