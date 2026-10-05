class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicktionary = defaultdict(list)

        for word in strs:
            alphakey = [0] * 26

            for letter in word:
                alphakey[ord(letter) - ord('a')] += 1
            
            dicktionary[tuple(alphakey)].append(word)
        
        return list(dicktionary.values())