import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
if sum(arr):        # 모두 0 이면 답은 N
    hash = {}
    for i in range(N):      # 인덱스 저장
      hash[arr[i]] = i
    cnt = 0
    for i in range(N):
        for j in range(N):
          add = arr[i] - arr[j] 
          if i!= j and add in hash and hash[add] != i and hash[add] != j:       # 자신이 아닌 숫자와 뺐을 때, 값이 뺀값과 자신이 아니면서 hash내부에 있으면 ++
            cnt += 1
            break       # 하나만 있어도 좋은 수
    print(cnt)
else:
    print(N)