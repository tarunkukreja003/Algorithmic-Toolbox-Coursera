#python3

def max_pairwise_product(n_numbers):
    n_numbers.sort(reverse=True)
    return (n_numbers[0] * n_numbers[1])
        
        
if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int,input().strip().split()))[:n]
    print(max_pairwise_product(input_numbers))

