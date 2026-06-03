class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []

        alucard = {}

        for n in nums:
            alucard[n] = alucard.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for numero, count in alucard.items():
            buckets[count].append(numero)
        
        for idf in range(len(buckets)-1, 0, -1):
            for i in buckets[idf]:
                ans.append(i)
                if len(ans) == k:
                    return ans