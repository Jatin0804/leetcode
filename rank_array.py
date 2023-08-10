'''
1331. Rank Transform of an Array

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr1 = []
        arr1.extend(arr)
        print(arr)
        arr1.sort()
        print(arr)
        rank = [0]*len(arr)
        dic = {}
        rank1 = 0
        for i in arr1:

            if i not in dic:
                dic[i] = {}
                dic[i]["count"] = 1
                rank1 += 1
            else:
                count = dic[i]["count"]
                count += 1
                dic[i]["count"] = count

            dic[i]["rank"] = rank1

        ind = 0
        for i in arr:
            num = dic[i]["rank"]
            rank[ind] = num
            ind += 1

        print(dic)

        return rank


#time
class Solution(object):
    def arrayRankTransform(self, arr):
        c = 1
        d = dict()
        for i in sorted(list(set(arr))):
            d[i] = c
            c += 1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr
    

#
class Solution(object):
    def arrayRankTransform(self, arr):
        copy = sorted(arr)
        ranks = {}
        rank = 1
        # storing the rank of every elements in hashtable ranks
        for n in copy:
            if n not in ranks:
                ranks[n] = rank
                rank += 1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr
