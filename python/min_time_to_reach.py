'''
1870. Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time you have to reach the office. 
To commute to the office, you must take n trains in sequential order. 
You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.

Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, 
or -1 if it is impossible to be on time.
Tests are generated such that the answer will not exceed 10^7 and hour will have at most two digits after the decimal point.

Example 1:

Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example 2:

Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:

Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
 
'''


import math
import numpy as np
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if len(dist)-1 >= hour:
            return -1

        left = 1
        right = max(dist)*100000

        while left < right:
            mid = (left+right)//2
            time = 0

            for i in range(len(dist)-1):
                time += math.ceil(float(dist[i]) / mid)
            time += float(dist[-1]) / mid

            if time <= hour:
                right = mid
            else:
                left = mid + 1

        return left


# best time


class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if (len(dist) > math.ceil(hour)):
            return -1
        # time=dist*1/speed
        # want to return min speed of max time (maximin)
        dist = np.array(dist)
        left = 1
        right = math.pow(10, 7)
        while (left <= right):
            speed = int((left+right)/2)
            cd = dist/float(speed)
            last = ceil(cd[-1])-cd[-1]
            if (last == 1):
                last = 0
            if (np.sum(np.ceil(cd))-last-0.0000000001 > hour):
                left = speed+1
            else:
                minspeed = speed
                right = speed-1
        return minspeed
