'''
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''


class Solution(object):
    def canJump(self, nums):
        '''
        :type nums: List[int]
        :rtype: bool
        '''
        last_position = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
                last_position = i # Since we just need to reach to this new index
        return last_position == 0


#
class Solution(object):
    def canJump(self, nums):
        # Take curr variable to keep the current maximum jump...
        curr = nums[0]
        # Traverse all the elements through loop...
        for i in range(1, len(nums)):
            # If the current index 'i' is less than current maximum jump 'curr'...
            # It means there is no way to jump to current index...
            # so we should return false...
            if curr == 0:
                return False
            curr -= 1
            # Update the current maximum jump...
            # It’s possible to reach the end of the array...
            curr = max(curr, nums[i])
        return True
