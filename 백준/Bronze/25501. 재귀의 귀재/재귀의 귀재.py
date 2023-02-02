T = int(input())
for _ in range(T):
    S = input()
    def isPalindrome(S):
        return int(S == S[-1::-1])

    idx = 0
    cnt = 1
    while idx <= int(len(S)/2)-1:
        if S[idx] != S[-idx-1]:
            break
        else:
            cnt += 1
            idx += 1
    
    print(isPalindrome(S), cnt)