# Uses python3
import sys
import random


#### Dutch National Flag Algorithm

import random
def quick_sort3(arr, low, high):
    # one element
    if low == high:
        return arr
    
    if low < high:
        m1, m2 = 0, 0
        # pivot_index = random.randrange(low, high+1, 1)
        # arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
        (m1, m2) = partition3(arr, low, high)
        
        left_part = quick_sort3(arr, low, m1-1)
        right_part = quick_sort3(arr, m2+1, high)
        
        return arr

def partition3(arr, low, high):
    
    if high - low <= 1:
        if arr[high] < arr[low]:
            swap(arr[high], arr[low])
        return (low, high)
        
    mid = low
    pivot_value = arr[high]
    while(mid <= high):
        if arr[mid] < pivot_value:
            # print('before swap arr[mid]====={}, arr[low]========{}'.format(arr[mid], arr[low]))
            (arr[mid], arr[low]) = swap(arr[mid], arr[low])
            # print('after swap arr[mid]====={}, arr[low]========{}'.format(arr[mid], arr[low]))
            mid = mid + 1
            low = low + 1
        elif arr[mid] == pivot_value:
            mid = mid + 1
        elif arr[mid] > pivot_value:
            (arr[mid], arr[high]) = swap(arr[mid], arr[high])
            high = high - 1
    
    return (low, high-1)

def swap(ele_1, ele_2):
    ele_1, ele_2 = ele_2, ele_1 
    return (ele_1, ele_2)



    

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    arr = quick_sort3(a, 0, n - 1)
    for x in arr:
        print(x, end=' ')
