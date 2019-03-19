'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        comp_str = strs[0]
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) > 1:
            for i in range(1, len(strs)):
                for t_index in range(min(len(comp_str), len(strs[i]))+1):
                    if comp_str[:t_index] == strs[i][:t_index]:
                        prefix = comp_str[:t_index]
                comp_str = prefix
        return prefix

    def f1(self, strs):
        if (strs == [] or len(strs) == 0):
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

if __name__ == '__main__':
    # s = ["abab","aba","abc"]
    # s = ["dog","racecar","car"]
    # s = ["flower","flow","flight"]
    # s = []
    # s = ["c","c"]
    s = ["aaa", "aa", "aaa"]
    # s = ["aa", "aa"]
    solu = Solution()
    # pre = solu.longestCommonPrefix(s)
    pre = solu.f1(s)
    print(pre)