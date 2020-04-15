# Uses python3

def max_gold(W, n, arr_w):
    ## assigning value to each gold bar. 1kg gold bar has value $1
    ## value is same as weight since more the gold more the value
#     arr_v = arr_w
    
    value_table = [[0 for j in range(W + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        
        for w in range(1, W + 1):
            
            value_table[i][w] = value_table[i-1][w]
            
            if arr_w[i-1] <= w:
            
                val = value_table[i-1][w - arr_w[i-1]] + arr_w[i-1]
                
                if val > value_table[i][w]:
                    value_table[i][w] = val
            
    
    
    return value_table[n][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    arr_w = list(map(int, input().split()))
    max_val = max_gold(W, n, arr_w)
    print(max_val)
