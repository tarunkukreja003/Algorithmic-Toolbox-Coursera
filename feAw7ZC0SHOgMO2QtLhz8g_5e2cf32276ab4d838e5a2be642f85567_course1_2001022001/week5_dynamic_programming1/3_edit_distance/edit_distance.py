# Uses python3

### whenever you get into a problem that isme se konsa operation karna hai hame kya pta, try to solve using DP

def edit_distance(str1, str2):
    ## don't use the following to create a 2D array, it will make a shallow list
#     edit_distance = [[0] * (len(str2) + 1)] * (len(str1) + 1)
# remember that here the strs starts from edit_distance[1][0] and edit_distance[0][1]

    str1_len = len(str1) + 1
    str2_len = len(str2) + 1
    edit_distance = [[0 for i in range(str2_len)] for j in range(str1_len)]
    
    for i in range(1, str1_len):
        edit_distance[i][0] = i
    for j in range(1, str2_len):
        edit_distance[0][j] = j
    
    
    for i in range(1, str1_len):
        
        for j in range(1, str2_len):
            

            ## we do a +1 in dynamic programming because we always look at previously computed values and add +1 to it
            ## to get the current value

            ## here we are adding +1 to del/insert/mismatch the i, j element and to add to the edit_distance previously computed
            deletion = edit_distance[i-1][j] + 1 # here we'll add +1 to deletion to delete the extra str1[i]
            insertion = edit_distance[i][j-1] + 1
            mismatch = edit_distance[i-1][j-1] + 1
            match = edit_distance[i-1][j-1]
            
            ## do i-1 and j-1 for str because they are one behind
            if str1[i-1] == str2[j-1]:
                edit_distance[i][j] = min(deletion, insertion, match)
            else:
                edit_distance[i][j] = min(deletion, insertion, mismatch)
    return edit_distance[len(str1)][len(str2)]


if __name__ == "__main__":
    dist = edit_distance(input(), input())
    print(dist)
    
