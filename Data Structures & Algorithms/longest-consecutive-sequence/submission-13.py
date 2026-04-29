class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSET = set(nums)
        longest = 0 

        for i in range(len(nums)):
            length = 0
            while (nums[i] + length) in numSET:
                length += 1
            longest = max(longest, length)
        return longest