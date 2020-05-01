class Solution:
    def firstBadVersion(self, n):
        start=1
        end=n
        mid=(start+end)//2
        while((end-start)>1):
            if(isBadVersion(mid)==False):
                start=mid
                mid=(start+end)//2
            else:
                end=mid
                mid=(start+end)//2
        if(isBadVersion(start)==True):
            return start
        return end
