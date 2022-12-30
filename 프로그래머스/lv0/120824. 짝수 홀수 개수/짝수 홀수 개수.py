def solution(num_list):
    even_num = 0
    odd_num = 0
    for i in num_list:
        if i%2 ==0:
            even_num +=1
        else:
            odd_num +=1
    return [even_num, odd_num]