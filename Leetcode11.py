'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

class Solution:
    def maxArea(self, height):
        maxarea, l, r = 0, 0, len(height)-1 # 记录最大值，最左侧，最右侧
        while(l < r):
            maxarea = max(maxarea, min(height[l], height[r])*(r - l)) # 从记录值和后来的计算值比较，取最大
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return maxarea
# 方法的理念是从直觉出发，底边越长肯定越大，而应该收缩时，短边应该被更替而不是长边，所以每次计算都是更改短边
# 原理证明之后描述