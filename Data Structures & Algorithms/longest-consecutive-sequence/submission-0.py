class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setsAndTheCity = set(nums)
        maxInches = 0

        for peen in setsAndTheCity:
            if (peen - 1) not in setsAndTheCity:
                length = 1

                while (peen + length) in setsAndTheCity:
                    length += 1
                
                maxInches = max(maxInches, length)
        return maxInches
                        