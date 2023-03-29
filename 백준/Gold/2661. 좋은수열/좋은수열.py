def check(num):
    length = len(num)
    for idx in range(1, length//2 +1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def recursive(num):
    global N
    if len(num)==N:
        print(num)
        exit()
    for i in '123':
        if check(num + i):
            recursive(num + i)
    return

N = int(input())
recursive('1')