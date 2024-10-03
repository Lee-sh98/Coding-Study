import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
positives = list(filter(int(0).__lt__, arr))
zeros = list(filter(int(0).__eq__, arr))
negatives = list(filter(int(0).__gt__, arr))
result = 0
for i in range(0, len(positives), 2):
    if i == len(positives)-1:
        result += positives[i]
    else:
        add = positives[i]+positives[i+1]
        multiply = positives[i]*positives[i+1]
        result += max(add, multiply)

for i in range(len(negatives)-1, -1, -2):
    if i==0 and not zeros:
        result += negatives[i]
    elif i> 0:
        result += negatives[i]*negatives[i-1]
print(result)
