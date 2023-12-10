class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [2,3,1,1,4] => [1,1,1,1,1]
        # [3,2,1,0,4] => [1,1,1,1,0]
        
        [1, 2, 3, 2, 1, 0]
        [3,2,1,0,0]
        [4,]
        
        [2,3,2,1,0]
        [3,4,3,2,1]
        
        [2,5,0,0,0]
        [3,6,5,4,3]
        if len(nums) == 1: return True
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = max(nums[i], dp[i-1]-1)
            else:
                return False
        return True
