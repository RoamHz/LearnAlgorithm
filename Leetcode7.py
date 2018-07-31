'''
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could 
only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:    
        lst = list(str(x))
        revlst = lst[::-1]
        j = 0
        for i in revlst:
            j = j * 10 + int(i)
        if j > 2 ** 31 - 1:
            return 0
        else:
            return j
    else:
        x = -x
        lst = list(str(x))
        revlst = lst[::-1]
        j = 0
        for i in revlst:
            j = j * 10 + int(i)
        if j < -2 ** 31:
            return 0
        else:
            return -j

if __name__ == '__main__':
    x = -123
    y = reverse(x)
    print(y)
