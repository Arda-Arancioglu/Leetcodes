class Solution:
    global Hashmap
    Hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D" :500,"M":1000}

    def romanToInt(self, s: str) -> int:
        def check(current:chr,next:chr) -> bool:
          if  Hashmap[current] < Hashmap[next] or current==next:
              print("true")
              return True
          else:
              print("false")
              return False

        s=s[::-1]
        sum=0
        i=0
        while i < (len(s)):
           
            if len(s)-i == 1:
                print("1st")
                sum += Hashmap[s[i]]
            elif check(s[i],s[i+1])== True:
                print("2nd")
                sum += Hashmap[s[i]]
            else:
                print("3rd")
                sum += Hashmap[s[i]] - Hashmap[s[i+1]]
                i+=1 
            print("sum is" ,sum)     
            i+=1                 

        return sum


s="CXIV"        
mysol=Solution()
print(mysol.romanToInt(s))
