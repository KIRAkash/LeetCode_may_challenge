"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space."""
def binaryseach(nums,start,end):
        mid=floor((start+end)/2)
        if(nums[mid]==nums[mid-1]):
            if((start+mid)%2==0):
                return binaryseach(nums,start,mid)
            else:
                return binaryseach(nums,mid+1,end)
        elif((mid+1)<len(nums) and nums[mid]==nums[mid+1]):
            if((start+mid)%2!=0):
                return binaryseach(nums,start,mid-1)
            else:
                return binaryseach(nums,mid,end)
        else:
            return nums[mid]
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        return binaryseach(nums,0,len(nums)-1)
