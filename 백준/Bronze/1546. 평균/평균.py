a = int(input())
b = input()

list = []
for i in b.split():
    list.append(int(i))

list_1 = []
for i in list:
    list_1.append(i/max(list)*100)

print(sum(list_1)/len(list_1))