class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # you make a hashmap here (a dictionary)
        myMap = {}

        # loop through. intead of it having to loop through until the very end
        # it can stop sooner than if you used a two pointer
        for i in range(len(nums)):
            # here you make the difference 
            diff = target - nums[i]
            if diff in myMap:
                return [myMap[diff], i]
            myMap[nums[i]] = i