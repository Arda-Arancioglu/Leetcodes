class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for str in s:
             
            if str == "(" or str == "[" or str == "{" :
                # print("appending",str,"to:\n",stack)
                stack.append(str)
            else:
                if len(stack)< 1 :
                    return False
                else:    
                    if str == ")" and stack[-1] == "(":
                        stack.pop()
                    elif str == "}"and stack[-1] == "{":
                        stack.pop()
                    elif str == "]"and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False    
        if len(stack) > 0:
            return False         
        else:            
            return True        
                        
                 
     
     
s="[]"
mySol = Solution()
print(mySol.isValid(s))        