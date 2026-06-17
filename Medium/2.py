# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        def unlinker (LL:Optional[ListNode]) -> int :
            myList = []
            sum = 0
            while LL != None: 
                myList.append(LL.val)
                LL=LL.next
            for i in range(len(myList)):
                sum += (10**i)* myList[i]
            return sum    

        def linker (Number:Optional[int]) -> Optional[ListNode]:
            BeforeList= [int(digits) for digits in str(Number)]
            # print(BeforeList)
            BeforeList.reverse()
            # print(BeforeList)
            dummy = ListNode()
            output = dummy
            for i in range(0,len(BeforeList)):
                output.val = BeforeList[i]
                if i == len(BeforeList)-1:
                    output.next = None
                else:
                    output.next= ListNode(BeforeList[i+1])
                output = output.next    
            return dummy
            

        wSum = unlinker(l1) + unlinker(l2)
        output = linker(wSum)
        # print(wSum)
        # print(output)

        return output
       
        
# below here is for testing purposes

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
mysol = Solution()
mysol.addTwoNumbers(l1,l2)