class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq = [[] for i in range(len(nums) + 1)] #creates list for bubble sort. creates range(len(nums)) + 1 arrays inside this array. [[], [], [], []]

        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        for i, c in hashMap.items():
            freq[c].append(i)
        
        res = []

        for j in range(len(freq) -1, 0, -1): 
            # last index -1, go down til 0, decrement by 1
            for n in freq[j]:
                res.append(n)
                if len(res) == k:
                    return res
        