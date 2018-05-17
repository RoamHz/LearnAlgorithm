# '''There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
# '''

# def median(A, B):
# 	m, n = len(A), len(B)
# 	#保证n为较长的那个list的长度
# 	if m > n:
# 		A, B, m, n = B, A, n, m
# 	if n == 0:
# 		raise ValueError

# 	#i用于查找长度为m的list
# 	imin, imax, half_len = 0, m, int((m+n+1)/2)
# 	#将A、B分为左右两部分，中值分别为i，j，则i+j为左部分总长，m-i+n-j为右部分总长
# 	#保证i+j=m-i+n-j
# 	#保证B[j−1]<=A[i] && A[i-1]<=B[j]，即左部分完全小于右部分(由于题目所给出的为递增的序列)
# 	while imin <= imax:
# 		i = int((imin + imax) / 2)
# 		#两个list合并长度的中值减去i
# 		j = half_len - i
# 		#如果B[j-1] > A[i]，说明A[i]太小，B[j-1]太大，A[i]应该在二分后的右边查找新的，同时减小j
# 		if i < m and B[j-1] > A[i]:
# 			imin = i + 1
# 		#如果A[i-1] > B[j]，说明A[i-1]太大，B[j]太小，A[i-1]应在二分后的左边查找新的，同时增大j
# 		elif i > 0 and A[i-1] > B[j]:
# 			imax = i - 1
# 		else:
# 			if i == 0:
# 				max_of_left = B[j-1]
# 			elif j == 0:
# 				max_of_left = A[i-1]
# 			else:
# 				max_of_left = max(A[i-1], B[j-1])
			
# 			if (m+n) % 2 == 1:
# 				return max_of_left
			
# 			if i == m:
# 				min_of_right = B[j]
# 			elif j == n:
# 				min_of_right = A[i]
# 			else:
# 				min_of_right = min(A[i], B[j])

# 			return (max_of_left + min_of_right)/ 2.0



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
    	nums1.extend(nums2)
    	nums1.sort()
    	length = len(nums1)
    	if length % 2 == 1:
    		mid = nums1[int(length/2)]
    		return mid
    	else:
        	mid = ( nums1[int(length/2 - 1)] + nums1[int(length/2)] ) / 2.0
        	return mid

if __name__ == '__main__':
	nums1 = [1, 3]
	nums2 = [2]
	so = Solution()
	print(so.findMedianSortedArrays(nums1, nums2))
