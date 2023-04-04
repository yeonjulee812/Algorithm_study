def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = rep[find_set(x)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 학생 수, M 신청서 수
    rep = [i for i in range(N+1)]
    arr = list(map(int, input().split()))
    tmp = set() # 대표원소 모음

    # union
    for i in range(M):
        union(arr[i*2+1],arr[i*2])

    # 대표원소 찾기
    for i in rep[1:]:
        tmp.add(find_set(i))

    print(f'#{tc} {len(tmp)}')
