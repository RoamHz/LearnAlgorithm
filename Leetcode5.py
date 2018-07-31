'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

# class Solution:
# 	def longestPalidrome(self, s):
# 		self.s = s
# 		lens = len(s)
# 		if lens <= 1:
# 			return s
# 		dp = [[False for i in range(lens)] for j in range(lens)]
# 		dp[lens][lens] = True
# 		for i in range(1, lens):
# 			dp[i][i] = True
# 			dp[i][i-1] = True
# 		resLeft, resRight = 0, 0
# 	    for k in range(2, lens):
# 	    	for i in range(lens-k):
# 	    		if s[i] == s[i+k-1] and dp[i+1][i+k-2]:
# 	    			dp[i][i+k-1] = True
# 	    			if resRight - resLeft < k:
# 	    				resLeft = i
# 	    				resRight = i+k-1
# 	    	return s[resLeft:resRight-resLeft+1]

# if __name__ == '__main__':
#     s = 'ababbaasdcsr' 
#     sou = Solution()
#     sou.longestPalidrome(s)
                    
class Solution:
    def longestPalindrome(self, s):
    	#Manacher算法
        if s == "":
            return (0, 1)
        t = "^#" + "#".join(s) + "#$"
        c = 0
        d = 0
        p = [0] * len(t)
        for i in range(1, len(t)-1):
        	#相对于中心c翻转下标i
            mirror = 2 * c - i   # = c - (i - c)
            p[i] = max(0, min(d-i, p[mirror]))
            #增加以i为中心的回文子串长度
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            #必要时调整中心点
            if i + p[i] > d:
                c = i
                d = i + p[i]
        (k, i) = max((p[i], i) for i in range(1, len(t)-1))
        return s[(i - k) // 2: (i + k) // 2]