import sys
input = sys.stdin.readline

def count_sort(arr, reverse=False):
    n = len(arr)
    M = max(arr)

    appearance = [0]*(M+1)
    result = [0]*n
    
    for a in arr:
        appearance[a] += 1
    
    i, count = 0, 0

    while i <= M:
        while appearance[i]:
            result[count] = i
            count += 1
            appearance[i] -= 1
        i += 1

    return result if not reverse else result[::-1]
    

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = count_sort(A)
B_sorted = count_sort(B, reverse=True)

S = sum(map(int.__mul__, A_sorted, B_sorted))

sys.stdout.write(str(S)+"\n")
