import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def preorder(in_left, in_right, post_left, post_right):
    if in_left>in_right:
        return

    root = postorder[post_right]

    root_idx = position[root]
    left_size = root_idx-in_left
    post_mid = post_left + left_size

    answer.append(str(root))
    preorder(in_left, root_idx-1, post_left, post_mid-1)
    preorder(root_idx+1, in_right, post_mid, post_right-1)
    

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = {v:idx for idx, v in enumerate(inorder)}

answer = []
preorder(0, n-1, 0, n-1)

print(" ".join(answer))
