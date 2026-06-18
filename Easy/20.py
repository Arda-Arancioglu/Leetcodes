class Solution:
    def isValid(self, s: str) -> bool:    
        MyList= []
        for i in range(len(s)):           
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                MyList.append(s[i]) 
            else:
                if not MyList:
                   return False
                top = MyList.pop()
                if s[i]==")" and top != "(":
                    return False
                if s[i]=="]" and top != "[":
                    return False
                if s[i]=="}" and top != "{":
                    return False
        return len(MyList)==0        
 

s="([)]"
mySol = Solution()
mySol.isValid(s)     