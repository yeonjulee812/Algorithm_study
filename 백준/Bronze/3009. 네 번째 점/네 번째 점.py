import sys

x_rac = {}
y_rac = {}
for _ in range(3):
    x, y = map(int, sys.stdin.readline().strip().split())
    if x not in x_rac.keys():
        x_rac[x] = 1
    else:
        x_rac[x] += 1
    if y not in y_rac.keys():
        y_rac[y] = 1
    else:
        y_rac[y] += 1
for i in x_rac.keys():
    if x_rac[i] < 2:
        res_x = i
for j in y_rac.keys():
    if y_rac[j] < 2:
        res_y = j
print(res_x, res_y)