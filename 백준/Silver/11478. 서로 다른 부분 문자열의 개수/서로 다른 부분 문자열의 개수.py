S = input()
s = len(S)

s1 = set()
for i in range(s): # 커서
    for j in range(s): # 개수
        s1.add(S[i:i+j+1])

print(len(s1))