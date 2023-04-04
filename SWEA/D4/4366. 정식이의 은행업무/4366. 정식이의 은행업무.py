T = int(input())
for tc in range(1,T+1):
    bi = list(map(int, input()))
    tri = list(map(int, input()))
    A = []

    for i in range(len(bi)): # bi의 각 자리 숫자를 살펴보는데
        num = 0
        bi[i] ^= 1 # i자리의 0을 1로, 1을 0으로 바꿈
        for x in bi: # 추측한 2진수를 10진수로 변환
            num = num*2 + x
        A.append(num)
        bi[i] ^= 1 # 원상복귀

    for i in range(len(tri)): # tri의 각 자리 숫자를 살펴보는데
        for j in range(3): # 0,1,2 중 하나로 바꿔
            num = 0
            if tri[i] != j:
                tmp = tri[i] # 원래 값 저장하고
                tri[i] = j
                for x in tri: # 추측한 3진수를 10진수로 변환
                    num = num*3 + x
                tri[i] = tmp
                if num in A: # A에 있으면 문제 해결!
                    ans = num
                    break

    print(f'#{tc} {ans}')
