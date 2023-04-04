def find_set(x): # 대표자 찾기
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y): # 합집합
    rep[find_set(y)] = rep[find_set(x)]

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split()) # V 마지막 노드번호, E 간선의 수
    rep = [i for i in range((V+1))] # 대표자 리스트 # makeset()
    li = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        li.append((n1,n2,w))

    # 가중치 기준으로 오름차순 정렬
    li.sort(key=lambda x:x[2])

    # 가중치 최소합 도출
    cnt, s = 0, 0
    for n1, n2, w in li:
        if find_set(n2) != find_set(n1):
            cnt += 1
            s += w
            union(n1,n2)
            if cnt == V:
                break

    print(f'#{tc} {s}')
