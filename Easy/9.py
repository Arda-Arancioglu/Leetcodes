class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        
        if stringX == stringX[::-1]:
            
            return True
        else:
            return False


x=1914
mysol = Solution()
print(mysol.isPalindrome(x))     