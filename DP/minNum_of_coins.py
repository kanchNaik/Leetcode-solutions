"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

def minCoins(coins, amount):
    INF = float('inf')
    dp = INF * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] != INF else -1