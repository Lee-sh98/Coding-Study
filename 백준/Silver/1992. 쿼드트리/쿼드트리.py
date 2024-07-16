import sys
input = sys.stdin.readline

def quad_tree(arr):
    total = 0
    n = len(arr)
    
    for line in arr:
        total += sum(line)
    if total == 0:
        return "0"
    elif total == n**2:
        return "1"
    else:
        result = "("
        for i in [0, n//2]:
            for j in [0, n//2]:
                tmp = []
                for k in range(i, i+n//2):
                    tmp.append(arr[k][j:j+n//2])
                result += quad_tree(tmp)
                
        return result+")"

N = int(input())
data = [list(map(int, input().rstrip())) for _ in range(N)]
result = quad_tree(data)

print(result)
