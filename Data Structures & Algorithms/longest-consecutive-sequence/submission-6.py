class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashSet = set(nums)

        for i in hashSet:
            if (i - 1 not in hashSet):
                length = 1
                while ((i + length) in hashSet):
                    length += 1
                longest = max(length, longest)
        return longest