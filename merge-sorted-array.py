#TC:O(len(nums1))
#SC:O(1)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1 #initialize pointer 1 as m-1
        p2 = n-1 #initialize pointer 2 as n-1
        p3 = m+n-1 #initialize pointer 3 as m+n-1
        
        while p1>=0 and p2>=0: #traverse until p1 is greater than 0 and p2 is greater than 0
            if nums1[p1]>nums2[p2]: # if p1 num is greater than p2, them assign the number at p3 with num at p1
                nums1[p3]=nums1[p1] 
                p1-=1#decrement p1
            else:
                nums1[p3]=nums2[p2] #else assign the number at p3 with num at p2
                p2-=1 #decrement p2
            p3-=1  #decrement p3
            
        if p2>=0:
            nums1[:p2+1]=nums2[:p2+1] #now after changing the values, just change the nums1 upto p2 with nums2 upto p2
            
        
        