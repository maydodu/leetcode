class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
a = Solution()
print(a.climbStairs(5))
