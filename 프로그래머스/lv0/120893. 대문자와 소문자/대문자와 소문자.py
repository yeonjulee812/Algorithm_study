def solution(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == my_string[i].lower():
            my_string[i] = my_string[i].upper()
        else:
            my_string[i] = my_string[i].lower()
    return ''.join(my_string)