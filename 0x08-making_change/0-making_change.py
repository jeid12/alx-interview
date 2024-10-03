#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)  # Use a large value to represent impossible amounts
    dp[0] = 0  # No coins are needed to make the total of 0
    
    # Loop through each amount from 1 to total
    for i in range(1, total + 1):
        # For each coin, update dp[i] if using that coin results in fewer coins
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still float('inf'), it means we cannot make the total
    return dp[total] if dp[total] != float('inf') else -1


