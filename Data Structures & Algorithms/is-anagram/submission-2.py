class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        alphabet = [0] * 26

        if len(s) != len(t):
            return False

        for letter in range(len(s)):
            alphabet[ord(s[letter]) - ord('a')] += 1
            alphabet[ord(t[letter]) - ord('a')] -= 1
        
        for val in alphabet:
            if val != 0:
                return False
        return True