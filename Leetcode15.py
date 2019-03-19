'''
Given an array nums of n integers, 
are there elements a, b, c in nums 
such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
'''

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 前一个数和后一个数相同则跳过，防止重复
                continue
            l, r = i+1, len(nums)-1 # 最小两个和一个最大值求和
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # <0说明小值太小
                    l +=1 
                elif s > 0: # >0说明大值太大
                    r -= 1
                else: # ==0
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res


if __name__ == '__main__':
    solu = Solution()
    # lst = [-1, 0, 1, 2, -1, -4]
    lst = [-2,0,0,2,2]
    answer_lst = solu.threeSum(lst)
    print(answer_lst)