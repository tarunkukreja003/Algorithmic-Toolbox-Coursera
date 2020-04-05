# Uses python3
def get_fibonacci_last_digit(n):
    first, sec, fib_last_digit = 0, 1, 0
    
    if n<=1:
        return n
    
    else:
        i = 2
        while i <= n:
            fib_last_digit = (first + sec) % 10
            first = sec
            sec = fib_last_digit
            i +=1
    

        return fib_last_digit
    
    

    

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
