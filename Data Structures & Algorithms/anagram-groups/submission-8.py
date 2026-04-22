class Solution:
    def charValues(self, string):
        value = [0] * 26
        for i in range(len(string)):
            value[(ord(string[i]) - ord('a'))] += 1
        return value
        



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)

        for word in strs:
            key = self.charValues(word)
            dictt[tuple(key)].append(word)
        
        return list(dictt.values())