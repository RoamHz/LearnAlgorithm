#无重复字符的最长子串
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lengthOfLongestSubstring(s):
	queue = []
	num = 0
	maxnum = 0
	for i in range(len(s)):
		if s[i] not in queue:
			queue.append(s[i])
			num += 1
			# print(queue, num)
			if maxnum < num:
				maxnum = num
		else:
			for k in range(queue.index(s[i])+1):
				queue.pop(0)
			queue.append(s[i])
			# print(queue)
			num = len(queue)
	return maxnum

if __name__ == '__main__':
	s = 'pwwkew'
	maxnum = lengthOfLongestSubstring(s)
	print(maxnum)