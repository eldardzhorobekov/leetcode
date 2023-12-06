class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([c for c in "{0:b}".format(n) if c == '1'])
