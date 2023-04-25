N = int(input())
li = list(map(int, input().split()))
li.sort()
cnt = 0

for i in range(N):
    new_li = li[:i] + li[i+1:]
    l, r = 0, N-2
    while l < r:
        s = new_li[l] + new_li[r]
        if li[i] == s:
            cnt += 1
            break
        if li[i] < s:
            r -= 1
        elif li[i] > s:
            l += 1

print(cnt)
