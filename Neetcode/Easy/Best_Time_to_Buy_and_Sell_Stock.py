class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      

        buy=0               #head
        sell=1              #tail
        profit=0
        maxpt=0
        while sell < len(prices):

            profit= prices[sell]-prices[buy]
            if profit > maxpt:
                maxpt= profit
                
            if prices[buy] > prices[sell]:
                buy = sell

            sell+=1
               
        
        return maxpt

prices=[5,1,5,6,7,1,10]
mySol = Solution()
print(mySol.maxProfit(prices))      




