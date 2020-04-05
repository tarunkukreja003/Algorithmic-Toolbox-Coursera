# Uses python3
import sys

# def binary_search(a, x):
#     left, right = 0, len(a)
#     # write your code here

def binarySearch (arr, l, r, x): 
# Check base case 
    if r >= l: 

        mid = l + (r - l) // 2

# If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 

# If element is smaller than mid, then it 
# can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

# Else the element can only be present # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 

    else: 
        # Element is not present in the array 
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    sorted_arr = data[1:]
    data_element_to_find = list(map(int, input().split()))
    m = data_element_to_find[0]
    ele_to_find_arr = data_element_to_find[1:]

        
    for key in ele_to_find_arr:
        res = binarySearch(sorted_arr, 0, len(sorted_arr)-1, key) 
        print(res, sep=' ', end=' ', flush=True)
