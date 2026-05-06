class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftPrefix = [0] * len(nums)
        rightPrefix = [0] * len(nums)
        
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            leftPrefix[i] = currentSum
        
        currentSumRight = 0
        for j in range(len(nums) - 1, -1, -1):
            currentSumRight += nums[j]
            rightPrefix[j] = currentSumRight
        
        for k in range(len(nums)):
            if leftPrefix[k] == rightPrefix[k]:
                return k
            else:
                continue
        
        return -1
        