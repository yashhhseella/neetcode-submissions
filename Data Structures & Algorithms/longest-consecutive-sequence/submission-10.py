class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        curr = 0

        for n in nums:
            if n - 1 not in nums:
                sub = 1
            
                while n + sub in nums:
                    sub += 1
            
                curr = max(sub, curr)
        return curr
            

        