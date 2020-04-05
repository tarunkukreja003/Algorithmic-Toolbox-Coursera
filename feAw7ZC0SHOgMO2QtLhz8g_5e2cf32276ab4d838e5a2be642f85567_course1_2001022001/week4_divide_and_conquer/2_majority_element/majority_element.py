# Uses python3
import sys

# [2, 9, 9, 3, 9, 6, 9, 9, 6]

def majority_element(arr, low, high):
    ## base case -> only 1 element present in the array, that is the majority element
    ## if 2 elements are present we can pick any of them
    if low == high:
        return arr[low]
    mid = low + (high - low) // 2
    left = majority_element(arr, low, mid)
    right = majority_element(arr, mid + 1, high)
    
    if left == right:
        return left
    
    left_count = sum(1 for i in range(low, high + 1) if arr[i] == left)
    right_count = sum(1 for i in range(low, high + 1) if arr[i] == right)
    
    
    return left if left_count > right_count else right
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    resulting_ele = majority_element(arr, 0, len(arr)-1)
    resulting_ele_count = sum(1 for i in range(0, len(arr)) if arr[i] == resulting_ele)
    if resulting_ele_count > (len(arr) // 2):
        print(1)
    else:
        print(0)
