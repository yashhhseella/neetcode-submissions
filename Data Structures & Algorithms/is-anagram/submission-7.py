class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        alphabet = [0] * 2600

        for i in range(len(s)):
            alphabet[ord(s[i])] += 1
            alphabet[ord(t[i])] -= 1
        
        for b in alphabet:
            if b != 0:
                return False

        return True
