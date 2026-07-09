class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for L in range(len(nums)):
            for R in range(L+1, len(nums), 1):
                if nums[L] == nums[R] and abs(L - R) <= k:
                    return True
            continue
        return False
                
        