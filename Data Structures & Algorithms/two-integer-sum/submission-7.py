class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            needed = target - n
            if needed in hashMap:
                return [hashMap[needed], i]
            hashMap[n] = i