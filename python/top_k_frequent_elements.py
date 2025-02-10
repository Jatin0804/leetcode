'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
        sorted(nums)
        num = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        while k > 0:

            list1 = list(dic.keys())
            list2 = list(dic.values())

            x = max(list2)
            y = list2.index(x)
            z = list1[y]
            num.append(z)
            dic[z] = 0
            k -= 1

        return num

        # # dic={}
        # # c=[]
        # # for i in nums:
        # #     c.append(nums.count(i))
        # #     if i not in dic:
        # #         dic[i]=1
        # #     else:
        # #         dic[i]+=1
        # # print dic
        # # c=list(set(c))
        # # print c
        # # nums=[]
        # # nums.append()
        # g1=0
        # g2=0
        # c=[]
        # num=[]

        # for i in nums:
        #     c.append(nums.count(i))
        # # for i in nums:
        # #     if nums.count(i)==max(c):
        # #         g1=i
        # #         c[i]=0
        # # for i in nums:
        # #     if nums.count(i)==max(c):
        # #         g2=i
        # while(k>0):
        #     x=max(c)
        #     y=c.index(x)
        #     num.append(nums[y])
        #     print c
        #     for i in range(len(c)):
        #         if c[i]==x:
        #             print i
        #             c[i]=0
        #     print c
        #     k-=1

        # return num
