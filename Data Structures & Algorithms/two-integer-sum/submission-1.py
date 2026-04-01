class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in h:
                return [h[remainder], index] # we do it this way because we want
            h[value] = index # the index's and not the actual values returned