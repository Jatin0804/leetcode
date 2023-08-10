'''
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).
 Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        '''
        n=len(ast)-1
        i=0
        while True and n>=0 and i<n:
            if n==0:
                return ast
            if ast[i] > 0 and ast[i+1] > 0:
                pass
            elif ast[i] < 0 and ast[i+1] < 0:
                pass
            elif ast[i] > 0 and ast[i+1] < 0:
                if abs(ast[i]) == abs(ast[i+1]):
                    del ast[i+1]
                    del ast[i]
                    n-=2
                elif abs(ast[i]) < abs(ast[i+1]):
                    del ast[i]
                    n-=1
                else:
                    del ast[i+1]
                    n-=1
            elif ast[i] < 0 and ast[i+1] > 0:
                if abs(ast[i]) == abs(ast[i+1]):
                    del ast[i+1]
                    del ast[i]
                    n-=2
                elif abs(ast[i]) < abs(ast[i+1]):
                    del ast[i]
                    n-=1
                else:
                    del ast[i+1]
                    n-=1
            
            i+=1
            print ast
        '''
        j = 0
        n = len(asteroids)

        for i in range(n):
            asteroid = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1

            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid
                j += 1
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1
        return asteroids[:j]


#
class Solution:
    def samesign(self, x, y):
        if x < 0 and y < 0:
            return True
        elif x > 0 and y > 0:
            return True
        return False

    def asteroidCollision(self, a):
        n = len(a)
        st = []
        for i in range(n):
            if len(st) == 0 or (st[-1] < 0 and a[i] > 0) or self.samesign(st[-1], a[i]):
                st.append(a[i])
            else:
                while len(st) > 0 and st[-1] > 0 and st[-1] < abs(a[i]):
                    st.pop()

                if len(st) == 0 or st[-1] < 0:
                    st.append(a[i])
                elif st[-1] == abs(a[i]):
                    st.pop()

        return st


#
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for i in asteroids:
            # Checking whether the aesteroid is heavier then the previously stored aesteroids -- pop from stack
            while stack and (stack[-1] >= 0 and i < 0) and abs(stack[-1]) < abs(i):
                stack.pop()
            # Checking whether the aesteroid is lighter then the previously stored aesteroids -- > add it
            if not (stack) or (stack[-1] < 0 and i >= 0) or (stack[-1] >= 0 and i >= 0) or (stack[-1] <= 0 and i <= 0):
                stack.append(i)
            else:
                # Checking whether the aesteroid is equal to the previously stored aesteroids -->
                if stack and abs(stack[-1]) == abs(i):
                    stack.pop()

        return stack
