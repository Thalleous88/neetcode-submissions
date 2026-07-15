class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(day, cooldown, check):
            if (day, cooldown, check) in memo:
                return memo[(day, cooldown, check)]

            if day >= len(prices):
                return 0

            buy = float('-inf')
            sell = float('-inf')
            skip = float('-inf')

            if check:
                sell = prices[day] + dp(day+1, 1, 0)
                skip = dp(day+1, 0, 1)
            elif cooldown:
                skip = dp(day+1, 0, 0)
            elif not cooldown:
                buy = dp(day+1, 0, 1) - prices[day]
                skip = dp(day+1, 0, 0)

            profit = max(buy, sell, skip)
            memo[(day, cooldown, check)] = profit
            

            return profit

        return dp(0, 0, 0)

            
            