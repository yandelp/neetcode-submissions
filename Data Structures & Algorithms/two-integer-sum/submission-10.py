class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a map
        #parse through the map with i, store value of nums[i] in n
        # create soemthing to hold target - currNum
        # if diff in map, return both indexes (map[diff], i)
        # outside of if, add to map

        m = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in m:
                return [m[diff], i]
            m[n] = i
        return