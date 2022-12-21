
def solution(numbers):
    list = []
    for i in numbers:
        for j in numbers:
            list.append(i*j)
    del list[list.index(max(list))]
    return max(list)