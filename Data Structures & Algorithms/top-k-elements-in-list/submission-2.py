class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = {}
        ans = []

        # we want to get the frequency of every number and then 
        # reorder the numbers in most to least frequency 

        for n in nums:
            buckets[n] = buckets.get(n, 0) + 1 # we have to set the number and increment on this side because if it isnt there we have to add it to the dictionary first and then we have to increment based on the number in there we cannot do this with a list
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in buckets.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


