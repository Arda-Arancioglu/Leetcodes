class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
            print("Testing the list:\n", strs)
            Repeatedprefix = ""
            
            strs = list(set(strs))
            print("Remove duplicates:\n",strs)

            def smallestWordfinder(strs:list[str])-> int:
                smallestWord = len(strs[0])
                for i in range(len(strs)):
                    if len(strs[i]) < smallestWord:
                        smallestWord = len(strs[i])
                return smallestWord        

            if  len(strs) == 0:
                return Repeatedprefix
            elif len(strs) == 1 :
                return strs[0]
            else:

                smallestWord = smallestWordfinder(strs)
                print("The smallest word is this long:",smallestWord) 

                for i in range(smallestWord):
                    currentLetter = strs[0][i]
                    for k in range(1,len(strs)):
                        if currentLetter != strs[k][i]:
                            return Repeatedprefix
                    Repeatedprefix += currentLetter
                          
                return Repeatedprefix


strs=["flower","flow","flight"]
mySol = Solution()
print("This is the longest comon prefix \"", mySol.longestCommonPrefix(strs),"\"")