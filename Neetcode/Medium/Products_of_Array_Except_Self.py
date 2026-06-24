class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def leftMultiplication(nums:list[int])-> list[int]:
            leftList=[1]
            sum= 1
            for i in range(len(nums)-1):
                sum *= nums[i]
                leftList.append(sum)
            return leftList        

        def rightMultiplication(nums:list[int])-> list[int]:
            rightList=[]
            sum=1
            for i in range(len(nums)-1):
                sum *= nums[len(nums)-1-i]
                rightList.append(sum)

            rightList = rightList[::-1]
            rightList.append(1)
            return rightList   
        thelist=[]
        if len(nums) < 2:
           return nums[::-1]      
        i=0
        left = leftMultiplication(nums)
        right= rightMultiplication(nums)
        print(left)
        print(right)
        while i < len(nums):
            thelist.append(left[i]*right[i])
            i+=1
        return thelist

nums=[-1,0,1,2,3]
mySol = Solution()
print(mySol.productExceptSelf(nums))
