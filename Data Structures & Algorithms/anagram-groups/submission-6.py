class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            value = [0] * 26
            for char in word:
                value [ord(char) - ord('a')] += 1
            dictionary[tuple(value)].append(word)
        
        return list(dictionary.values())
                