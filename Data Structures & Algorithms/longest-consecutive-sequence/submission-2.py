class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setsAndTheCity = set(nums)
        penis = 0

        for n in setsAndTheCity:
            if n - 1 not in setsAndTheCity:
                length = 1
                while n + length in setsAndTheCity:
                    length += 1
                penis = max(length, penis)
        return penis


        