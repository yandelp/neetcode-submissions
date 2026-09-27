class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create list for bucket sort, map for count (index)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # parse through nums, index shall be occurances, list of nums at that index shall be nums that occur that many times

        for n in nums:
            # populating count map
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            #populating freq
            freq[c].append(n)

        #create result array
        res = []

        #parse through freq array backward
        for i in range(len(freq) - 1, 0, -1):
            # for each number in [[this part], [], []]
            for n in freq[i]:
                # append the number to result. this will be highest number on the first pass.
                res.append(n)
                if len(res) == k:
                    #when we get to k length for result, return result (guaranteed output)
                    return res

