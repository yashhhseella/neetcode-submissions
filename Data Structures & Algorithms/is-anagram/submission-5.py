class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        alphaBett = [0] * 26

        for i in range(len(s)):
            alphaBett[ord(s[i]) - ord('a')] += 1
            alphaBett[ord(t[i]) - ord('a')] -= 1
        
        for i in alphaBett:
            if i != 0:
                return False
        return True

        