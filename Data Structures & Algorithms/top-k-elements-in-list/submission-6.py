class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count which will be stored [[here]]
        # frequency array which will have indexes as # of occurances and value as numbers that have i occurances.
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # append all needed values to map and 2d arr
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        