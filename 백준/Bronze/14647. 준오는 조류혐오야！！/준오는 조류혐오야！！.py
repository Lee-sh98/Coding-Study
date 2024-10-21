import sys
input = sys.stdin.readline

def count(line):
    return "".join(line).count("9")

n, m = map(int, input().split())

arr = [list(input().split()) for _ in range(n)]
row_count = list(map(count, arr))
col_count = list(map(count, zip(*arr)))

if max(row_count)>max(col_count):
    row = max(range(n), key=row_count.__getitem__)
    print(sum(row_count)-row_count[row])
else:
    col = max(range(m), key=col_count.__getitem__)
    print(sum(col_count)-col_count[col])
