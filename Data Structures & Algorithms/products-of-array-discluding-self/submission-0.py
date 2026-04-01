class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = (len(nums)) * [1]

        prefix = 1
        for n in range(len(nums)):
            ans[n] = prefix
            prefix *= nums[n]
        postfix = 1
        for n in range(len(nums)-1, -1, -1):
            ans[n] *= postfix
            postfix *= nums[n]
        return ans