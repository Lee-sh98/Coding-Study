def solution(arr):
    first = last = -1
    
    for i in range(len(arr)):
        if first == -1 and arr[i] == 2:
            first = i
        if arr[i] == 2:
            last = i
    
    if first == last == -1:
        return  [-1]
    elif first == last:
        return [2]
    else:
        return arr[first:last+1]
    