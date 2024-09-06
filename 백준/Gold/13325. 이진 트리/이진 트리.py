import sys
input = sys.stdin.readline

def dfs(i):
    global answer
    if i>=2**k:
        answer += tree[i]
        return tree[i]

    left = dfs(2*i)
    right = dfs(2*i+1)
    
    answer += tree[i] + abs(left-right)

    return tree[i] + max(left, right)

k = int(input())
tree = [0, 0]+list(map(int, input().split()))
answer = 0

dfs(1)
print(answer)
