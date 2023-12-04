class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        x=3 => 11
        y=1 => 1
        """
        ans = 0
        while x or y:
            x_ost = x % 2
            y_ost = y % 2
            if x_ost != y_ost:
                ans += 1
            x //= 2
            y //= 2
        return ans
