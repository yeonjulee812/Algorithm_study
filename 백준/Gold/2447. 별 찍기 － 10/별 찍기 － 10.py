N = int(input())

def star(N):
    if N == 3:
        return ['***', '* *', '***']

    arr = star(N//3) # 원본(이전 단계에 출력된 별 리스트)
    stars = [] # 출력할 리스트
    
    for i in arr: # 첫번째 구간
        stars.append(i*3)
    
    for i in arr: # 두번째 구간(가운데 빈칸)
        stars.append(i + ' '*(N//3) + i)
    
    for i in arr: # 세번째 구간
        stars.append(i*3)
    
    return stars

print('\n'.join(star(N)))

# 리스트에 append해서 한번에 출력
# 인덱스에러 피하기 위해 새로운 리스트를 만들어서 append하자!