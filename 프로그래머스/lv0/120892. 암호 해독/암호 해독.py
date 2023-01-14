def solution(cipher, code):
    answer = []
    for num, char in enumerate(cipher):
        if (num+1)% code ==0:
            answer.append(char)
    return ''.join(answer)