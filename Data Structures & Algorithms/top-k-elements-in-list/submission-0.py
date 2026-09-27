class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        return sorted(hashMap, key=hashMap.get, reverse=True)[:k]