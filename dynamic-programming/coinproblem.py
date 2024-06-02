# okay so here is how the problem goes... 
# given a set of coins with values = {c_1, c_2, ...} and a target sum of money m 
# what is the minimum number of coins needed to form that sum m ?? 

# well one idea can be to choose the largest coin first and keep going wellllll

# example coins = {1, 4, 5}
# target sum = 13 

# so if we were to use that strategy then it would look something like 

# 5 5 1 1 1 = 13 cents however a better solution would be 

# 4 4 4 1 which is only 4 coins 

# What is then the subproblem that we should be aiming to solve ? 


# KEY -- dynamic programming is a little bit like a brute force? 

# How would we go about brute forcing this problem in the first place ? ? 

# We could try every single possibility right ... what would that look like 


#                                        (13) 
#             5                          4                        1    
#            (8)                        (9)                      (12)
#         5  4  1                      5  4  1                  5  4  1 
#        (3)(4)(7)                     


# so something like this where we try every possible combination to see if it works out
# and I assume that we can use memoization to store these subproblems such as 
# 8 choose 5 which will show up multiple times in the tree above 