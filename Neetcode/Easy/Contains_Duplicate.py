class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        #hashmap ?
        myHash = {}
        for i in nums:  
            if myHash.get(i) != None :
                return True
            else:
                myHash.update({i:1})
        return  False

nums =[1,2,3,3]
mySol = Solution()
print(mySol.hasDuplicate(nums))    