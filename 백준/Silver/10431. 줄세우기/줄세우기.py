import sys

input = sys.stdin.readline

def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    else:
        start = 0
        end = len(arr)
        mid = (start+end)//2
        left = merge_sort(arr[start:mid])
        right = merge_sort(arr[mid:end])
        i = j = 0
        tmp = []
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                cnt += len(left[i:])
                j += 1
        if i == len(left):
            tmp += right[j:]
        if j == len(right):
            tmp += left[i:]

        return tmp




for _ in range(int(input())):
    t, *kids = map(int, input().strip().split())
    cnt = 0
    merge_sort(kids)
    print(f'{t} {cnt}')