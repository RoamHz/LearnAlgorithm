'''
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        numlst = []
        num = x
        if x < 0:
            return False
        else:
            while(x!=0):
                numlst.append(x%10)
                x = x // 10
        newnum = 0
        for i in numlst:
            newnum = newnum * 10 + i
        if newnum == num:
            return True
        else:
            return False