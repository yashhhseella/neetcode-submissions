class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        ans = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= prefix # we need to do this because we need to modify the ans array from the right side as well as compute
            # not the same as prefix since that we do the multiplication in one and set
            prefix *= nums[i]
        
        return ans

        