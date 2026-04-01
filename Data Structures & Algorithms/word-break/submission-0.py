class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        truthy = [False] * (len(s) + 1)

        truthy[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    truthy[i] = truthy[i + len(word)]
                if truthy[i]:
                    break
        
        return truthy[0]