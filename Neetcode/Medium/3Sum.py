class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        #2pointers
        myList=[]
        head=0
        tail=len(nums)-1
        i=0
        k=0
        # if nums.count(0) >= 3:
        #     myList.append([0,0,0])
        while i < len(nums)-2:
            head=i+1
            tail = len(nums)-1
          
            if nums[i-1] == nums [i] and i > 0:
                i+=1
            else:    
                while head < tail :
                    sum=nums[i]+nums[head]+nums[tail]
                    if sum==0:
                        myList.append([nums[i],nums[head],nums[tail]])
                        while nums[head+1] == nums[head] and head < tail-1:
                            head+=1
                        while nums[tail-1] == nums[tail] and head < tail-1:
                            tail-=1
                        head+=1
                        tail-=1    
                    elif sum > 0:
                        tail-=1
                    elif sum < 0:
                        head += 1
                i+=1
        return myList    
       


nums=[-1,0,1,2,-1,-4]
mySol = Solution()
print(mySol.threeSum(nums))        