class Solution:

    def encode(self, strs: list[str]) -> str:
        sending =""
        for i in strs:
            sending +=str(len(i))+"#"+i
        return sending


    def decode(self, s: str) -> list[str]:
        i=0
        j=0
        MyList=[]
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1

            length = int(s[i:j])

            myWord=s[j+1:length+1+j]
            
            MyList.append(myWord)
            i = j + 1 +length

        return MyList  
       
          

            




strs=["neet","code","love","you"]
mySol = Solution()
x=mySol.encode(strs)
print(x)
y=mySol.decode(x)
print(y)