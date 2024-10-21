import sys
input = sys.stdin.readline

def count(line):
    result = 0
    for s in line:
        for c in s:
            result += c=="9"

    return result

n, m = map(int, input().split())

arr = [list(input().split()) for _ in range(n)]
row_count = list(map(count, arr))
col_count = list(map(count, zip(*arr)))

if max(row_count)>max(col_count):
    row = max(range(n), key=row_count.__getitem__)
    arr[row] = ["0"]*m
else:
    col = max(range(m), key=col_count.__getitem__)
    for i in range(n):
        arr[i][col] = "0"

print(sum(map(count, arr)))
