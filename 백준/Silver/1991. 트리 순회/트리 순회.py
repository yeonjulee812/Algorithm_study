N = int(input())
left = [0]*(N+1)
right = [0]*(N+1)
for _ in range(N):
    p, c1, c2 = input().split()
    if left[ord(p)-64] == 0 and c1.isalpha():
        left[ord(p)-64] = ord(c1)-64
    if right[ord(p)-64] == 0 and c2.isalpha():
        right[ord(p)-64] = ord(c2)-64


def preorder(i):
    print(chr(i+64), end = '')
    if left[i]:
        preorder(left[i])
    if right[i]:
        preorder(right[i])
    return

preorder(1)
print()
def inorder(i):
    if left[i]:
        inorder(left[i])
    print(chr(i+64), end = '')
    if right[i]:
        inorder(right[i])
    return

inorder(1)
print()
def postorder(i):
    if left[i]:
        postorder(left[i])
    if right[i]:
        postorder(right[i])
    print(chr(i+64), end = '')
    return

postorder(1)


