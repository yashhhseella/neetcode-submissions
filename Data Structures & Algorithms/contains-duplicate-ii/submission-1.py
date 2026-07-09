class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for L in range(len(nums)):
            for R in range(L+1, len(nums), 1):
                if abs(L - R) > k:
                    break
                
                if nums[L] == nums[R]:
                    return True
            L += 1
        return False
                
        