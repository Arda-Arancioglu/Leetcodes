class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        myMap= {}
        finalList=[]
        for i in nums:
            if i not in myMap:
                myMap[i] = 1
            else:
                myMap[i] += 1

        total = k
        bestkey=0
        bestval=0
        
        while total > 0: 
            bestkey=0
            bestval=0       
            for key,val in myMap.items():
                if val > bestval:
                    bestkey = key
                    bestval = val
            finalList.append(bestkey)    
            myMap[bestkey] = -1    

            total-=1
        return finalList        




nums = [1,3,4,4,2,7,4,55,5,5]
k=2
mySol = Solution()
print(mySol.topKFrequent(nums,k))
