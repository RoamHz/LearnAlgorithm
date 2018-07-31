'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''
# string convert(string s, int numRows);
class Solution:
    def convert(self, s, numRows):
        lst = [ ['0' for i in range(len(s) // 2 + 1)] for j in range(numRows) ]
        offset = numRows - 1
        istr = 0
        j = 0
        k = 0
        ss = ''
        if numRows == 1 or len(s) == 1:
            ss = s
        else:
            while(istr < len(s)-1):
                for i in range(numRows):
                    if istr < len(s):
                        lst[i][k] = s[istr]
                        istr += 1
                k += 1
                for j in range(k, k+offset):
                    i -= 1
                    if istr < len(s):
                        lst[i][j] = s[istr]
                        istr += 1
                istr -= 1
                k += offset-1
        for i in range(numRows):
            for j in range(len(s) // 2 + 1):
                if lst[i][j] != '0':
                    ss += lst[i][j]

        return ss

def main():
	s = 'ABC'
	numRows = 2
	sol = Solution()
	ss = sol.convert(s, numRows)
	print(ss)

if __name__ == '__main__':
	main()