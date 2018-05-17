class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        #时间复杂度O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        #         else:
        #             continue

        #时间复杂度O(n)
        arr = {}
        length = len(nums)
        for i in range(length):
            if (target-nums[i]) in arr:
                return arr[target-nums[i]], i
            arr[nums[i]] = i
                    
def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    i, j = solution.twoSum(nums, target)
    print(i, j)

if __name__ == "__main__":
    main()