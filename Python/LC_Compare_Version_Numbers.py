class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        
        Approach:
        
        split the numbers and store it as a list.
        Iterate through both the lists and keep comparing.
        If v1>v2: return(1)
        If v2>v1: return(-1)
        If we reach the end of the lists and if both are same up until that point, return(0).
        """
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i<len(versions1) else 0
            v2 = versions2[i] if i<len(versions2) else 0
            if(v1>v2):
                return(1)
            elif(v2>v1):
                return(-1)
        return(0)
            
