'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums1=nums1+nums2
        nums1=sorted(nums1)
        if len(nums1)%2 == 0:
            return (float(nums1[len(nums1)/2])+float(nums1[(len(nums1)/2)-1]))/2
        else:
            return (nums1[len(nums1)/2])

if __name__ == '__main__':
   sol = Solution()
   nums1=[1,2,3]
   nums2=[2,3,4]
   print(sol.findMedianSortedArrays(nums1,nums2))

