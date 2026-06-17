class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
               
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
