class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            # print(s)
            
            if len(s) == 0:
                return len(s)
            elif len(s) == 1:
                return len(s)
            elif len(s) == 2:
                if s[0] == s[1]:
                    return 1
                else:
                    return 2
            else:
                k=0
                
                word = ""
                BiggestSubstring = ""

                while k < len(s):    

                    CheckLetters = set(s)
                    # print(CheckLetters)
                    word = ""
                    for i in range (k, len(s)):
                        
                        current = s[i]
                        
                        # print("word:",word)
                        # print("current:",current)

                        if CheckLetters == {}:
                            break

                        if i == k :
                            CheckLetters.remove(current)
                            word += current
                            # print("removed ", current , " \n",CheckLetters)
                        
                        if i+1 < len(s):                                                        
                            next = s[i+1]
                            # print("next:",next)
                            if current == next or next not in CheckLetters:
                                if len(word) > len(BiggestSubstring):
                                    BiggestSubstring = word
                                    # print("THE BIGGEST:" ,BiggestSubstring)
                                break
                            else:
                                CheckLetters.remove(next)
                                # print("removed ", next , " \n",CheckLetters)
                                
                                word += next
                                # print("word:",word)
                        else:
                            break
                        if len(word) >= len(BiggestSubstring):
                            BiggestSubstring = word
                            # print("THE BIGGEST:" ,BiggestSubstring)
                    k+=1
                return len(BiggestSubstring)     


                  


s ="nugsipopcpsbvqrvuwdvgwehvfkwhldvhlpqcfhfxcgsuzqovtkbsqknwwjdjnaqarid"
mySol = Solution()
print(mySol.lengthOfLongestSubstring(s))