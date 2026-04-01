class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        current = 0
        for i in nums:
            if i == 1:
                current += 1
            elif i == 0:
                total = max(total, current)
                current = 0
        
        return max(total, current)