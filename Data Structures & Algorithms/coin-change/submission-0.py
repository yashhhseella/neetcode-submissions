class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            ans = 100000

            for coin in coins:
                if amount - coin >= 0:
                    ans = min(ans, 1 + dfs(amount - coin))
                
            memo[amount] = ans

            return ans

        minCoins = dfs(amount)

        return -1 if minCoins >= 100000 else minCoins
        