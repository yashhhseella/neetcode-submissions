class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmapp = {} # have a hashset here

        for i, n in enumerate(nums): # index, number
            diff = target - n # calculate the diff

            if diff in hashmapp:
                return [hashmapp[diff], i]
            else:
                hashmapp[n] = i