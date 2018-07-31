'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''

MIN = -2**31
MAX = 2**31 -1
import re
# def myAtoi(str):
#     """
#     :type str: str
#     :rtype: int
#     """
#     str = str.strip(' ')
#     MIN = -2**31
#     MAX = 2**31 -1
#     numlst = []
#     if str == '':
#         return 0
#     for i in str.split(' '):
#         try:
#             i = float(i)
#             numlst.append(i)
#         except Exception:
#             pass
#     if numlst[0] < MIN:
#         print(MIN)
#     elif numlst[0] > MAX:
#         print(MAX)
#     else:
#         print(numlst[0])



# def myAtoi(str):
#     MIN = -2**31
#     MAX = 2**31 -1
#     if not str:
#         return 0
#     str = str.strip()
#     number, flag = 0, 1
#     if str[0] == '-':
#         str = str[1:]
#         flag = -1
#     elif str[0] == '+':
#         str = str[1:]
#     for c in str:
#         if c >= '0' and c <= '9':
#             number = 10 * number + ord(c) - ord('0')
#         else:
#             break
#     number = flag * number
#     number = number if number <= MAX else MAX
#     number = number if number >= MIN else MIN


def myAtoi(str):
    str = str.strip()
    str = re.findall('(^[\+\-0]*\d+)', str)
    try:
        result = int(''.join(str))
        # print(result)
        if result > MAX > 0:
            return MAX
        elif result < MIN < 0:
            return MIN
        else:
            return result
    except:
        return 0


if __name__ == '__main__':
    s = '42 sdg 56 74574 '
    atoi = myAtoi(s)
    print(atoi)