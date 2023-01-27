N, M = map(int, input().split())

# 행렬 입력
matrix1 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix2.append(row)

matrix = []
for i in range(N):
    final_row = []
    for j in range(M):
        final_row.append(matrix1[i][j]+matrix2[i][j])
    matrix.append(final_row)

for i in range(N):
    print(*matrix[i], sep = ' ')