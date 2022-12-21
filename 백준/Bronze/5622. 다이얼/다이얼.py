num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
list_1 = list(input())
result = 0
for i in list_1:
    for j in num:
        if i in j:
            result += num.index(j) +3
print(result)