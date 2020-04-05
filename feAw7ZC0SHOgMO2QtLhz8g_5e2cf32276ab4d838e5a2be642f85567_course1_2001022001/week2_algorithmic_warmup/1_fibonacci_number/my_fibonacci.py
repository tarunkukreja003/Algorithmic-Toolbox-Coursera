# Uses python3
def calc_fib(n):
    first, sec, third = 0, 1, 0
    
    if n<=1:
        return n
    
    else:
        i = 2
        while i <=  n:
            third = first + sec
            first = sec
            sec = third
            i +=1
    

        return third
    
n = int(input())
print(calc_fib(n))
