'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 = s1+i.lower()

        print(s1)
        return s1 == s1[::-1]

#fast regex
import re
class Solution(object):
    def isPalindrome(self, s):
       new_s = re.sub(r"[^a-zA-Z0-9\\s+]","",s).lower()

       return new_s==new_s[::-1]
    

# faster regex
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[\W_]+', '', s).lower()

        # Check if the modified string is a palindrome
        return s[:] == s[::-1]


#
class Solution(object):
    def isPalindrome(self, s):
       start = 0
       end = len(s)-1

       while (start < end):
           first = s[start]
           last = s[end]
           if not first.isalnum():
               start += 1
           elif not last.isalnum():
               end -= 1
           elif first.upper() != last.upper():
               return False
           else:
               start += 1
               end -= 1

       return True
