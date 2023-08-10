'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if nums[0] == nums[n/2]:
            return nums[0]
        elif nums[n/2] == nums[n-1]:
            return nums[n-1]
        else:
            return nums[n/2]
