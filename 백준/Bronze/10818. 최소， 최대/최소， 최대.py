a = int(input())
list = input()
list_1 = []

for i in list.split():
    list_1.append(int(i))

print(min(list_1), max(list_1))