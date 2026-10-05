class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphalist = [0] * 26

        if len(s) != len(t):
            return False

        for letter in range(len(s)):
            alphalist[ord(s[letter]) - ord('a')] += 1
            alphalist[ord(t[letter]) - ord('a')] -= 1
        
        for i in range(26):
            if alphalist[i] != 0:
                return False
        return True
        