'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        dic={}
        dic1={}
        for i in len(s):
            ch=
            print dic
        for i in t:
            dic1[i]=0
        
        print dic
        print dic1
        return true
        """
        lens=len(s)
        lent=len(t)
        if lens!=lent:
            return False
        lis=[0]*lens
        lis1=[0]*lent
        # print s[0]
        for i in range(0,lens):
            if lis[i]!=0:
                continue
            else:
                lis[i]=i+1
                for j in range(lens-1,i,-1):
                    if s[i] != s[j]:
                        continue
                    else:
                        lis[j]=lis[i]
        for i in range(0,lent):
            if lis1[i]!=0:
                continue
            else:
                lis1[i]=i+1
                for j in range(lent-1,i,-1):
                    if t[i] != t[j]:
                        continue
                    else:
                        lis1[j]=lis1[i]
        print lis
        print lis1
        return True if lis==lis1 else False
    
#better

class Solution(object):
    def isIsomorphic(self, s, t):
        map1=[]
        map2=[]

        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        return True if map1==map2 else False
    
#best


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, c in enumerate(s):
            if c in d:
                if t[i] != d[c]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                d[c] = t[i]
        return True
