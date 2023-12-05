class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx: int, cur: List[int]) -> None:
            if idx == len(nums):
                ans.append(cur[:])
                return
            
            helper(idx+1, cur)
            
            cur.append(nums[idx])
            helper(idx+1, cur)
            cur.pop()

        ans = []
        helper(0, [])
        return ans

