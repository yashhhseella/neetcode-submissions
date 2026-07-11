class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dupe = set()

        L = 0

        for R in range(len(nums)):
            if R - L > k: # checking for window length
                dupe.remove(nums[L])
                L += 1 # incrementing if too big
            if nums[R] in dupe: # this is the equal case since window
                                # set would contain the dupe value
                return True
            dupe.add(nums[R]) # adding elements to the window
        
        return False # end condition