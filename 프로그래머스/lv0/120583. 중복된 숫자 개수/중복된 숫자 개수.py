def solution(array, n):
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
        else:
            cnt += 0
    return cnt            