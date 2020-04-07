# Uses python3

########## Money Change using Dynamic Programming
  
def dp_change(money):
    coin_sorted_array = [1, 3, 4]
    min_no_of_coins = []
    if money <= 0:
        return 0
    min_no_of_coins.append(0)
    
    for m in range(1, money+1):
        min_no_of_coins.append(10000) # min_no_of_coins[m] = 10000
        
        for i in range(len(coin_sorted_array)):
            if m >= coin_sorted_array[i]:
                num_of_coins = min_no_of_coins[m - coin_sorted_array[i]] + 1
            if num_of_coins < min_no_of_coins[m]:
                min_no_of_coins[m] = num_of_coins
    return min_no_of_coins[money]
            


if __name__ == '__main__':
    n = int(input())
    min_number_coins_n = dp_change(n)
    print(min_number_coins_n)
