class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list) # defaultdict so unitted keys of the  
        #                         signature are OK for append in the hashmap

        for word in strs: # iterate thru all words in list
            signature = [0] * 26 # count mathmatical value of each word
            for letter in word: # iterate thru all leters in word
                signature[ord(letter) - ord('a')] += 1 # add 1 for each letter in word
            ans[tuple(signature)].append(word) # add the word to the key of the signature
        return list(ans.values()) # return all values of the hashmap in a list
        