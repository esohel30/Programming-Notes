# now that we covered memoization, how can we restructure the solution so 
# that we do not use function calls ? 


def fib(n): 

    memo = {} 

    for i in range(1, n + 1): 

        if i <= 2: 
            result = 1  
        else: 
            result = memo[i - 1] + memo[i - 2]

        memo[i] = result 

    return memo[n]

# so here we need to be smart about the direction we go about.
# this is a bottom up approach. We solve the problems in a progressive fashion
# till we get to the main value 

