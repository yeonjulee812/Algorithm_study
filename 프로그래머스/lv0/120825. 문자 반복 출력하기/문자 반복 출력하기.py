def solution(my_string, n):
    list = []
    for i in range(len(my_string)):
        list.append(my_string[i]*n)
    return ''.join(list)    