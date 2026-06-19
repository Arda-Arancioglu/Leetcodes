class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sToMap(s:str)-> dict:
                myMap = {}
                for i in s :
                    if  i not in myMap.keys():
                        myMap[i] = 1
                    else:               
                        myMap[i] += 1
                return myMap
        
        if len(s) != len(t):
            return False
        
        else:
            if sToMap(s) == sToMap(t):
                return True
            else:
                return False
           
            


       

s="asdfasd"
t="sasdfad"
mySol= Solution()
print(mySol.isAnagram(s,t))        