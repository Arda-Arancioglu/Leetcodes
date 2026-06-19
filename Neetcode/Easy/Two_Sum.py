class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        myMap = {}
        print(list(enumerate(nums)))
        for i,num in enumerate(nums):
            
            if  target - num in myMap:
                return [myMap[ target - num],i]
            myMap[num] = i
        return False    



nums=[1,3,4,2,6,7]
target=5
mySol = Solution()
print(mySol.twoSum(nums,target))    