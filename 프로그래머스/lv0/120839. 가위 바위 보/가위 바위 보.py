def solution(rsp):
    answer = []
    for i in rsp:
        if i == '2':
            answer.append('0')
        if i == '0':
            answer.append('5')
        if i == '5':
            answer.append('2')
    return ''.join(answer)