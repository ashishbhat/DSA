# Python program to count number of 
# ways to reach nth stair.

# Recursive function to count number
# of ways to reach nth stair
def countWaysRecur(n, memo):
    
    # Base case for 0th stair
    if n == 0:
        return 1
    
    # For invalid stair, return 0.
    if n < 0:
        return 0
    
    # If n'th stair is memoized,
    # return its value
    if memo[n] != -1:
        return memo[n]

    # Count number of ways to reach (n-1), (n-2),
    # (n-3)th stair and memoize it.
    memo[n] = countWaysRecur(n - 1, memo) + \
    countWaysRecur(n - 2, memo) + countWaysRecur(n - 3, memo)
    return memo[n]

def countWays(n):
    memo = [-1] * (n + 1)
    return countWaysRecur(n, memo)

if __name__ == "__main__":
    n = 5
    print(countWays(n))