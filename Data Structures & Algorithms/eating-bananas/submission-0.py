class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        leastRate, maxRate = 1, max(piles)
        ans = maxRate

        while leastRate <= maxRate:
            midRate = (leastRate + maxRate) // 2
            t = 0
            for bananas in piles:
                t += math.ceil(bananas / midRate)
            if t <= h:
                ans = midRate
                maxRate = midRate - 1
            else:
                leastRate = midRate + 1
        return ans
                
            
            

        