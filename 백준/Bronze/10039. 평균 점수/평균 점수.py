import sys
input = sys.stdin.readline

arr = [max(int(input()), 40) for _ in range(5)]
print(sum(arr)//5)
