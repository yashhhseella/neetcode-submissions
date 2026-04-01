class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(char for char in s.lower() if char.isalnum())
        l, r = 0, len(s) - 1

        if not s:
            return True

        while l < r:
            if s[r] != s[l]:
                return False
            l += 1
            r -= 1
        return True
        