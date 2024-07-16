import sys
input = sys.stdin.readline

def merge_sort(l, r):
    global arr
    if l<r:
        m = (l+r)//2
        merge_sort(l, m)
        merge_sort(m+1, r)
        merge(l, m, r)
    

def merge(l, m, r):
    global arr, stored
    i, j, t = l, m+1, 0
    merged = []
    while i<=m and j<=r:
        if arr[i] <= arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1
    
    while i<=m:
        merged.append(arr[i])
        i += 1

    while j<=r:
        merged.append(arr[j])
        j += 1
    i = l
    for m in merged:
        arr[i] = m
        i += 1
    stored += merged

stored = []
N, K = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(0, len(arr)-1)
if K<len(stored):
    print(stored[K-1])
else:
    print(-1)
