class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashbrown = {}

        for i in range(len(nums)):
            if nums[i] in hashbrown:
                return [hashbrown[nums[i]], i]
            else:
                remainder = target - nums[i]
                hashbrown[remainder] = i
            
        