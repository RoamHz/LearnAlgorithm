class Solution():
    def longestPalidrome(self, s):
        # Dynamic Programming
        length = len(s)
        maxl = 0
        start = 0
        for i in range(length):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]

        # Expand Around Center
        def expandAroundCenter(s, left, right):
            L, R = left, right
            while L >= 0 and R < length and s[L] == s[R]:
               L -= 1
               R += 1
            return R-L-1

        start, end = 0, 0
        length = len(s)
        for i in range(length):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > end - start:
                start = i - (maxlen - 1) / 2
                end = i + maxlen / 2
        return s[start: end+1]

        #Manacher's Algorithm
        


if __name__ == '__main__':
    s = 'abbasdaffa'
    solu = Solution()
    print(solu.longestPalidrome(s))
                    