#TC: O(n)
#SC: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0 #set the maximum as zero
        l =0 #set the left pointer to zero
        r = len(height)-1  #set the right pointer to zero
        while l<r: #traverse until left is less than right
            #max area is going to be the maximum between the prev max and minimum between left height and right hieght multiplied with (difference b/w right and left)
            maxi = max(maxi,(min(height[l],height[r])*(r-l))) 
            if height[l]< height[r]: #if left height is less than right height, increase left height, else increase right height
                l=l+1 
            else:
                r= r-1
        
        return maxi #return the maximum