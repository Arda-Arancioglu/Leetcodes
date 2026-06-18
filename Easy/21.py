from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def unlink(myList:Optional[ListNode] )-> list[int]:
            TheList = []
            
            while myList != None:
                TheList.append(myList.val)
                myList = myList.next
                
            return TheList    

        def link ( myList: list[int] )-> Optional[ListNode]:
            dummy = ListNode()
            TheList = dummy 
           
            for i in myList:
                TheList.next = ListNode(i)
                TheList = TheList.next

            return dummy.next

        MyList =  list(unlink(list1)+ unlink(list2))
        MyList.sort()
   

        return link(MyList)


           

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(6)))
mySol=Solution()
mySol.mergeTwoLists(list1,list2)       
