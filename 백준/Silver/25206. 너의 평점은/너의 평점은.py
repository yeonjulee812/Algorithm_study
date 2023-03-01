import sys

total = tmp = 0

for _ in range(20):

    name, score, gpa = sys.stdin.readline().strip().split()
    if gpa == 'P':
        continue
    total += float(score)

    if gpa == 'A+':
        tmp += float(score) * 4.5
    elif gpa == 'A0':
        tmp += float(score) * 4
    elif gpa == 'B+':
        tmp += float(score) * 3.5
    elif gpa == 'B0':
        tmp += float(score) * 3
    elif gpa == 'C+':
        tmp += float(score) * 2.5
    elif gpa == 'C0':
        tmp += float(score) * 2
    elif gpa == 'D+':
        tmp += float(score) * 1.5
    elif gpa == 'D0':
        tmp += float(score)
    
print(tmp/total)