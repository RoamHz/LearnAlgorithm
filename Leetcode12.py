'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''


class Solution:
    def intToRoman(self, num):
        romanOut = ''
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        Roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                romanOut += Roman[i]
        return romanOut

if __name__ == '__main__':
    solu = Solution()
    s = solu.intToRoman(1994)
    print(s)