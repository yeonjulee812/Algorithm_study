import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node = [0] * (n + 1)
for i in range(n):
    node[inorder[i]] = i

def preorder(in_s, in_e,post_s,post_e):
    if in_s > in_e or post_s > post_e:
        return

    root = postorder[post_e]
    left = node[root] - in_s # 왼쪽 서브트리의 노드개수
    right = in_e - node[root] # 오른족 서브트리의 노드개수

    print(root, end=" ")
    preorder(in_s, in_s+left-1, post_s, post_s+left-1)
    preorder(in_e-right+1, in_e, post_e-right, post_e-1)

preorder(0, n-1, 0, n-1)