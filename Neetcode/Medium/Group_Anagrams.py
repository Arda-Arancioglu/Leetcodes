class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        BigList={}
        
        for i in strs:
            Mylist=[0]*26
            for k in i:
                index= ord(k) - ord("a")
                Mylist[index] += 1
            Mylist = tuple(Mylist)    
            if  Mylist in BigList:
                BigList[Mylist].append(i)
            else:
                BigList[Mylist] = [i]      

        return list(BigList.values())
                


strs=["act","pots","tops","cat","stop","hat"]
mySol=Solution()
print(mySol.groupAnagrams(strs))        