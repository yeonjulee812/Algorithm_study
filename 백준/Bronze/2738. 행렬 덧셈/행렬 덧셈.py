N, M = map(int, input().split())

# 첫번째 행렬
matrix1 = [list(map(int, input().split())) for _ in range(N)]
# 두번째 행렬
matrix2 = [list(map(int, input().split())) for _ in range(N)]
# 각 원소의 합 도출
for i in range(N):
    for j in range(M):
        matrix1[i][j]+= matrix2[i][j]
    print(*matrix1[i])