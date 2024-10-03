#!/usr/bin/python3
"""
This module contains the makeChange function that calculates
the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to meet with the coins.

    Returns:
        int: The fewest number of coins needed to meet total, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make the total of 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means we can't meet the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1


