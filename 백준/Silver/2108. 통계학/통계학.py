import sys
input = sys.stdin.readline

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

# 산술평균
print(round(sum(li)/len(li)))

# 중앙값
print(sorted(li)[(N-1)//2])

# 최빈값
cnt_li = [0]*8001 # 0 ~ 8000
for i in range(N):
    li[i] += 4000 # 모두 (0 또는) 양수로 만들기
for i in li:
    cnt_li[i] += 1 # 개수 세서 cnt_li에 담기
#
# maxCnt = 0
# for i in cnt_li:
#     if maxCnt < i:
#         maxCnt = i
maxCnt = max(cnt_li)

copy_li = []
for i in cnt_li:
    copy_li.append(i)

copy_li.remove(maxCnt) # 최빈값 중 최댓값을 인덱스로 갖는 원소 삭제

if maxCnt not in copy_li: # 최빈값이 유일한 값이면
    common_num = cnt_li.index(maxCnt) - 4000
else: # 최빈값이 여러 개면
    new_li = []
    for i in range(8001):
        if cnt_li[i] == maxCnt:
            new_li.append(i)
    common_num = new_li[1] - 4000

print(common_num)

# 범위
# maxV, minV = -4000, 4000
for i in range(len(li)):
    li[i] -= 4000
    # if maxV <= li[i]:
    #     maxV = li[i]
    # if minV > li[i]:
    #     minV = li[i]

print(max(li) - min(li))
