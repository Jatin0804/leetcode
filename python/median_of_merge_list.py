'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        size = len(nums1)-1
        med = 0.0
        if size % 2 == 0:
            med = nums1[size/2]
        else:
            print nums1[size/2]
            print nums1[size/2 + 1]
            med = (nums1[size/2] + nums1[size/2 + 1]) / 2.0
        return med
