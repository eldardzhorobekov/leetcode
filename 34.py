class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound() -> int:
            l, r = 0, len(nums)-1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    r = m - 1
                    ans = m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return ans

        def upper_bound() -> int:
            l, r = 0, len(nums)-1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    l = m + 1
                    ans = m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return ans
        
        if not nums:
            return [-1, -1]
        return [lower_bound(), upper_bound()]
