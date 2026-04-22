class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in diff:
                return [diff[remainder], i]
            
            diff[num] = i
        
        return []