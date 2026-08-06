class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_SET = set(nums)

        maxCount = 0


        for n in nums:
            count = 1
            if (n - 1) not in nums_SET:
                while (n + 1) in nums_SET:
                    n += 1
                    count += 1
                maxCount = max(count, maxCount)
            pass
        return maxCount
                




        