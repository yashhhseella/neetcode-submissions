class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charSet = set(s)

        ans = 0

        for c in charSet:

            L = 0
            windowLen = 0

            for R in range(len(s)):
                if s[R] == c:
                    windowLen += 1
                
                while (R - L + 1) - windowLen > k:
                    if s[L] == c:
                        windowLen -= 1
                    L += 1
                
                ans = max(ans, R - L + 1)
        
        return ans
                
                    