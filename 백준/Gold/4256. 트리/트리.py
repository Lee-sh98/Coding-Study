import sys
input = sys.stdin.readline


def postorder(pl, pr, il, ir):
    if pl>pr:
        return []
    if pl==pr:
        return [preorder[pl]]
    root = preorder[pl]
    idx = inorder.index(root)
    
    left_size = idx-il
    left = postorder(pl+1, pl+left_size, il, idx-1)
    right = postorder(pl+left_size+1, pr, idx+1, ir)
    
    return left+right+[root]
    

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    result = postorder(0, n-1, 0, n-1)
    print(*result)
