class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashbrown = {}

        for i, n in enumerate(nums):
            remainder = target - n
            if remainder in hashbrown:
                return [hashbrown[remainder], i]
            hashbrown[n] = i
        
        