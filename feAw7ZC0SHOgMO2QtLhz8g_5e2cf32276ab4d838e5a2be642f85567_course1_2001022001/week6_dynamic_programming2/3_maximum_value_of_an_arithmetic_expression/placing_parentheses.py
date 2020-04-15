# Uses python3
def calc(operand_1, operand_2, operator):
    if operator == '+':
        return (operand_1 + operand_2)
    elif operator == '-':
        return (operand_1 - operand_2)
    else:
        return (operand_1 * operand_2)

def get_max_min(table_max, table_min, i, j, operator_arr):
    min_i_j = 1000000
    max_i_j = -1000000
    
#     print('insie get_max_min i = {}, j = {} '.format(i, j))
#     print('table_max after getting inside get_max_min ', table_max)
    
    for k in range(i, j):
        a = calc(table_max[i][k], table_max[k+1][j], operator_arr[k])
        b = calc(table_max[i][k], table_min[k+1][j], operator_arr[k])
        c = calc(table_min[i][k], table_max[k+1][j], operator_arr[k])
        d = calc(table_min[i][k], table_min[k+1][j], operator_arr[k])
        
        
        if max_i_j < max(a, b, c, d):
            max_i_j = max(a, b, c, d)
        if min_i_j > min(a, b, c, d):
            min_i_j = min(a, b, c, d)
    
    return (max_i_j, min_i_j)
    
        

def paranthesis(operator_arr, ele_arr, n):
    table_max = [[0 for j in range(0, n)] for i in range(0, n)]
    table_min = [[0 for j in range(0, n)] for i in range(0, n)]
    
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                table_max[i][j] = int(ele_arr[i])
                table_min[i][j] = int(ele_arr[i])
                
    ### its upper triangle of the matrix where column >= row 
    ## s is just the difference between j and i
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            table_max[i][j], table_min[i][j] = get_max_min(table_max, table_min, i, j, operator_arr)
            
            
    return table_max[0][n-1]



if __name__ == "__main__":
    expression_str = str(input())
    operand_array, operator_array = [], []
    for i in range(len(expression_str)):
    
        if i % 2 == 0:
            operand_array.append(expression_str[i])
        else:
            operator_array.append(expression_str[i])
    max_value = paranthesis(operator_array, operand_array, len(operand_array))
    print(max_value)