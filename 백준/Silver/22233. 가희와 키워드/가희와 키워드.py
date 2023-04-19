import sys
N, M = map(int, sys.stdin.readline().rstrip().split()) # N 메모장에 적은 키워드 개수, M 블로그에 쓴 글 개수
written = {}
cnt = 0
for _ in range(N):
    written[sys.stdin.readline().rstrip()] = True
for _ in range(M):
    for keyword in sys.stdin.readline().rstrip().split(','):
        try:
            if written[keyword]:
                N -= 1
                written[keyword] = False
        except:
            pass
    print(N)