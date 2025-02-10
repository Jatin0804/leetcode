class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        sign = -1 if x < 0 else 1

        x *= sign

        while x > 0:
            res = res * 10 + x % 10
            x //= 10

        if sign * res < -2**31 or sign * res > 2**31 - 1:
            return 0

        return res * sign
