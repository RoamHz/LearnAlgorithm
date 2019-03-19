'''
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
'''

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[len(nums)-1] 
        for i in range(len(nums)-2):
            start = i+1; end = len(nums)-1
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                if sums > target:
                    end -= 1
                else:
                    start += 1
                if abs(sums - target) < abs(result - target):
                    result = sums
        return result
                    