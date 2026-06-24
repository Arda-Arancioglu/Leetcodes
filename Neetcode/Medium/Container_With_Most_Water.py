class Solution:
    def maxArea(self, heights: list[int]) -> int:
        head=0
        tail=len(heights)-1
        maxy=0
        while head<tail:
            area = abs(min(heights[head],heights[tail])*(head-tail))
            
            if area > maxy:
                maxy = area
            if heights[head]>heights[tail]:
                tail-=1
            else:
                head+=1
 
        return maxy


heights=[1,7,2,5,4,7,3,6]
mySol = Solution()
print(mySol.maxArea(heights))       