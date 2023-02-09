A, B = map(int, input().split())
A_li = set(map(int, input().split()))
B_li = set(map(int, input().split()))

print(len(A_li.union(B_li) - A_li.intersection(B_li)))