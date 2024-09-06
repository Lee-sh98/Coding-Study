import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bs(arr, left, right, target):

    while left<=right:
        mid = (left+right)//2
        if target<arr[mid]:
            right = mid-1
        else:
            left = mid+1
    return left

    
def postorder(arr, left, right):
    if left > right:
        return

    root = arr[left]
    mid = bs(arr, left, right, root)

    postorder(arr, left+1, mid -1)
    postorder(arr, mid, right)
    print(root)

arr = []
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

postorder(arr, 0, len(arr)-1)
