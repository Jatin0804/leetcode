'''
2789. Largest Element in an Array after Merge Operations

You are given a 0-indexed array nums consisting of positive integers.

You can do the following operation on the array any number of times:

Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. Replace the element nums[i + 1] with nums[i] + nums[i + 1] 
and delete the element nums[i] from the array.
Return the value of the largest element that you can possibly obtain in the final array.
'''


class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        while True:
            i = 0
            cont = 0
            while i <= n:
                if i+1 > n:
                    break
                if nums[i] <= nums[i+1]:
                    nums[i+1] = nums[i]+nums[i+1]
                    del nums[i]
                    n -= 1
                    print(nums)

                # if nums[i]>nums[i+1]:
                #     return nums[0]
                i += 1
                # if nums[i]==nums[-1]:
                #     return 0
            if n == 0:
                return nums[0]
            for j in range(len(nums)-1):
                if nums[j] <= nums[j+1]:
                    cont = 1
                    break

            if cont == 0:
                return nums[0]

                # if cont==2:
                #     return nums[0]
                # else:
                #     break

            cont = 0


#
class Solution:
    def maxArrayValue(self, nums):
        a = []  # Create a new list to store the updated values

        size = len(nums)

        for i in range(size):
            # Copy the elements from the input list to the new list
            a.append(nums[i])

        for i in range(len(a) - 1, 0, -1):
            if a[i - 1] <= a[i]:  # If the previous element is less than or equal to the current element
                # Update the previous element by adding the current element
                a[i - 1] = a[i] + a[i - 1]

        return max(a)  # Find the maximum element in the list and return it


#singel line

class Solution(object):
    def maxArrayValue(self, nums):
        return reduce(lambda curr, num: curr + num if num <= curr else num, reversed(nums))
