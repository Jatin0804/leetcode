'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) + 1
        l = s = 0
        for r, v in enumerate(nums):
            s += v
            while s >= target:
                s -= nums[l]
                res = min(res, r-l+1)
                l += 1

        return 0 if res > len(nums) else res
    
#


class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = j = sum1 = 0
        ans = 1000000

        while j < len(nums):
            sum1 += nums[j]

            while sum1 >= target:
                ans = min(ans, j-i+1)
                sum1 -= nums[i]
                i += 1

            j += 1

        return 0 if ans == 1000000 else ans


#
class Solution(object):
    def minSubArrayLen(self, target, nums):
        # initialize pointers and sum
        left, right, total = 0, 0, 0
        # initialize minimum length to be the length of the array plus 1 (invalid)
        min_len = len(nums) + 1

        # loop through the array
        while right < len(nums):
            # add current number to the sum
            total += nums[right]
            # move right pointer
            right += 1

            # check if the sum is greater than or equal to target
            while total >= target:
                # update minimum length if necessary
                min_len = min(min_len, right - left)
                # subtract left number from the sum and move left pointer
                total -= nums[left]
                left += 1

        # if minimum length is still the initialized value, there is no valid subarray
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
