class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array1 = [0] * 26
        array2 = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            array1[ord(s[i]) - ord('a')] += 1
            array2[ord(t[i]) - ord('a')] += 1
        
        for i in range(len(array1)):
            if array1[i] == array2[i]:
                continue
            else:
                return False
        
        return True