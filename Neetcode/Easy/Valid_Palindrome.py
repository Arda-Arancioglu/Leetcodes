class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str=""
        #removing non alphanumeric chars
        for i in s:
            if i.isalnum() == True:
                str += i


        print(str)
        head =0
        tail= len(str)-1

        while head < (len(str)-1)/2:
            if str[head] == str[tail]:
                head+=1
                tail-=1
            else:
                return False   
        
        return True

s="Was it a car or a cat I saw?"
mySol = Solution()  
print(mySol.isPalindrome(s))      