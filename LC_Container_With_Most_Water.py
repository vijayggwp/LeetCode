class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l = 0
        r = len(height) - 1
        while(l<r):
            if(height[l]<height[r]):
                maxarea = max(maxarea, height[l]*(r-l))
                l+=1
            else:
                maxarea = max(maxarea, height[r]*(r-l))
                r-=1
        return(maxarea)
