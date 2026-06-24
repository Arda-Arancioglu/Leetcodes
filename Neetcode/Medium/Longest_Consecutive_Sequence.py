class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:   
        # Below is an O(nlogn) algorithm 
        nums = list(set(nums))#remove repeared 
        nums.sort() #O(nlogn)
        head=0
        tail = 1
        i=1
        maxsum=0
        sum=0
        print(nums)
        if len(nums) < 2:
            return len(nums)
        while i < len(nums):
            
            if nums[head]+1==nums[tail]:
                sum +=1
                if sum > maxsum :
                    maxsum = sum
                head+=1
                tail+=1     
            else:
                sum=0
                head = tail
                tail += 1             
              

            i+=1

        return maxsum+1
    
nums  =[1,0,-1]
mySol = Solution()
print(mySol.longestConsecutive(nums))
        