class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        # left pointer all the way on the left
        # right pointer all the way on the right

        while l < r:
            # go until reach a letter
            # the logic is inversed, we check if it is a letter
            # or number and if it is we stop
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # then check if the letter is equal
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
    
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


