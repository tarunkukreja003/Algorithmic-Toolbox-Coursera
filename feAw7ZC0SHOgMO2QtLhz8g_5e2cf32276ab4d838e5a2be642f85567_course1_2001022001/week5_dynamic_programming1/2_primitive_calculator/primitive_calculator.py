# Uses python3
import sys

# greedy approach
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

# dynamic programming approach
### when using if-elif ladder, else is necessary, only when we use if, then else is not necessary
# approach --> min_ops(10) = min{min_ops(10-1), min_ops(10//2), min_ops(10//3)}
def min_ops(n):
    min_operations, intermediate_arr = [0, 0], []
    
    intermediate_num_dict = {}
    for i in range(2, n+1):
        min_operations.append(1000001)
        
        b, c = 10000001, 10000001
        
        a = min_operations[i - 1] + 1
        if (i % 2) == 0:
            b = min_operations[i//2] + 1
        if (i % 3) == 0:
            c = min_operations[i//3] + 1
            
        min_arr = [a, b, c]
        
        min_num = 10000002
        for ele in min_arr:
            if ele < min_num:
                min_num = ele
   
        min_operations[i] = min_num
        
        
        if (min_operations[i] == a):
            intermediate_num_dict[i] = i - 1
        if (min_operations[i] == b):
            intermediate_num_dict[i] = i//2
        if (min_operations[i] == c):
            intermediate_num_dict[i] = i//3
 
    
    key = n
    while key > 1:
        intermediate_arr.append(key)
        key = intermediate_num_dict[key] # value
    intermediate_arr.append(1)

    return (min_operations[n], intermediate_arr)

if __name__ == "__main__":
    n = int(input())
    min_ops, rev_intermediate_arr = min_ops(n)
    print(min_ops)
    j = len(rev_intermediate_arr) - 1
    while j != -1:
        print(rev_intermediate_arr[j], end=" ")
        j = j - 1


