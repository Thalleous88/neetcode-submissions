class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        def dp(i, coins, amount, memo):
            if amount == 0:
                return 0
            if amount < 0 or i >= len(coins):
                return float('inf')
            
            if memo[i][amount]:
                return memo[i][amount] 
            else:

                take = dp(i, coins, amount-coins[i], memo)
                skip = dp(i+1, coins, amount, memo)
                memo[i][amount] = min(1 + take, skip)

                return memo[i][amount]

        res = dp(0, coins, amount, memo)

        if res == float('inf'):
            return -1

        return res