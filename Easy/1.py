class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:    
               
        listoflists=[]
        lengthofSet=len(nums)
        for head in range(lengthofSet):
            i = head + 1
            if i > lengthofSet:
                continue
            else:
                while i != lengthofSet:
                    if nums[head] + nums[i] == target:
                        listoflists=[head,i]
                    i=i+1 
        return listoflists

nums = [1,4,3,2]
mySol = Solution()
print(mySol.twoSum(nums,5))