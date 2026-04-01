class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Lpane, Rpane = 0, 1
        maxProfit = 0

        while Rpane <= len(prices) - 1: #conditional for loop
            
            profit = prices[Rpane] - prices[Lpane]

            if profit < 0:
                Lpane = Rpane
            if profit >= 0:
                maxProfit = max(maxProfit, profit)
                Rpane +=1
        return maxProfit

        