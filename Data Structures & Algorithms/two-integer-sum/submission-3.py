class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashbrown = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashbrown:
                return [hashbrown[target - nums[i]], i]
            else:
                hashbrown[nums[i]] = i
        