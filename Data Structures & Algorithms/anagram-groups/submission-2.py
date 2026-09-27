class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map charCount to list of anagrams
        
        for s in strs:
            count = [0] * 26 # a-z (26 characters, 26 zeros)

            for c in s:
                count[ord(c) - ord("a")] += 1 # if a = 80, then b would be 81. 

            res[tuple(count)].append(s)

        return list(res.values())