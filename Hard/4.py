class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
            num = nums1 + nums2
            num.sort()
            # print(num)

            if len(num) % 2 == 0:
                # print ("even") 
                return ((num[int((len(num))/2)-1])+(num[int((len(num))/2)]))/2  
            else:
                # print("odd")
                return num[int((len(num)-1)/2)]      



nums1=[1,2]
nums2=[3,4]
mySol = Solution()
print(mySol.findMedianSortedArrays(nums1,nums2))        