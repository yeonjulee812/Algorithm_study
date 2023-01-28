# 행렬을 2차원 리스트에 담아주기
matrix = [list(map(int, input().split())) for _ in range(9)]
# 최댓값 도출
max_num = max(list(map((lambda x: max(x)), matrix)))
# 위치 출력

for row, row_list in enumerate(matrix):
    if max_num in row_list:
        that_row = row + 1
        for idx in range(9):
            if max_num == matrix[that_row-1][idx]:
                that_col = idx + 1

print(max_num)
print(that_row, that_col)