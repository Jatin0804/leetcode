'''
2765. Longest Alternating Subarray

You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:

m is greater than 1.
s1 = s0 + 1.
The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, 
and so on up to s[m - 1] - s[m - 2] = (-1)m.
Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,3,4,3,4]
Output: 4
Explanation: The alternating subarrays are [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.
Example 2:

Input: nums = [4,5,6]
Output: 2
Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.
'''

class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        elif len(nums)==2 and (nums[1]==nums[0]+1 ):
            return 2
        
        count1=0
        for i in range(1,len(nums)):
            j=i
            count=0
            if nums[j]==nums[j-1]+1:
                count+=2
                j+=1
                run=1
                while True and j<=len(nums)-1:
                    print ("j : ",j)
                    
                    if run%2==0:
                        if nums[j]==nums[j-1]+1:
                            count+=1
                        else:
                            break
                    else:
                        if nums[j]==nums[j-1]-1:
                            count+=1
                        else:
                            break
                    print ("count : ",count)
                    run+=1
                    j+=1
            count1=max(count1,count)
            print ("count1: ",count1)
        return count1 if count1!=0 else -1
    
#best


class Solution(object):
    def alternatingSubarray(self, nums):
        n = len(nums)

        res = dp = -1

        for i in range(1, n):
            if dp > 0 and nums[i] == nums[i-2]:
                dp += 1
            else:
                dp = 2 if nums[i] == nums[i-1] + 1 else -1
            res = max(res, dp)
        return res
