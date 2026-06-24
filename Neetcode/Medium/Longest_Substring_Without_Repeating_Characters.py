class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head=0
        tail=0
        max_length=0
        mySet=set()
        while tail < len(s) :
        
            

            if s[tail] not in mySet:
                mySet.add(s[tail])
                tail+=1

            else:
                mySet.remove(s[head])    
                head+=1

            length = tail-head

            if length > max_length:
                max_length=length    

        return max_length

s="aab"     
mySol=Solution()
print(mySol.lengthOfLongestSubstring(s))        