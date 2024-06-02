
def calc_fibonacci_naive(n): 
    if n <= 2: 
        return 1 
    else: 
        return calc_fibonacci_naive(n - 1) + calc_fibonacci_naive(n - 2)

# This is slow because we are performing redundant calculations 
# for example when we calculate fib(5) = fib(4) + fib(3) 
# fib(3) is actually calculated twice and fib(2) is calculated even more times
# these operations need only to be calculated once 

# solution using memoization 

# this is dictionary as the indicies need to be paired with the values 
memoo = {}

def fiby(n): 
    # we can check if the value we are looking for is in memo 

    if n in memoo: 
        return memoo[n]

    if n <= 2: 
        return 1 
    else:
        result = fiby(n - 1) + fiby(n - 2) 
    
    # How do we actually put the values into the dictionary however ? 
    memoo[n] = result 
    # ohhh is this why it is called a bottom up dp approach?? 
    return result 



# same solution without the clutter 

memo = {}

def fib(n): 

    if n in memo: 
        return memo[n]

    if n <= 2: 
        return 1 
    else: 
        result = fib(n - 1) + fib(n - 2)
    
    memo[n] = result 
    return result 

print(calc_fibonacci_naive(50))

