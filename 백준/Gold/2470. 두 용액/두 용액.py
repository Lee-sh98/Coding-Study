import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, len(arr)-1
prev = abs(arr[left]+arr[right])
result = [arr[left], arr[right]]

while 0<=left<right<N:
    lv, rv = arr[left], arr[right]
    total = lv+rv
    cur = abs(total)
    
    if cur<prev:
        result = [lv, rv]
        prev = cur
        
    if total<0:
        left += 1
    else:
        right -= 1
    
print(*result)
