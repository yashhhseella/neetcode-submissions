class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = set()
        L = 0
        lenth = 0

        for R in range(len(s)):
            while s[R] in memory:
                memory.remove(s[L])
                L += 1
            memory.add(s[R])
            lenth = max(lenth, len(memory))
        return lenth

        