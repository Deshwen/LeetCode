class Solution:
    def canJump(self, nums):
        end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
        if end == 0:
            return True
        else:
            return False