class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # store the result in the result array
        result = [1] * len(nums)

        # first pass to calculate the prefix
        prefix = 1  # 
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            result[i] = prefix

        # second pass to calculate the postfix
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]  # 
            result[i] *= postfix

        return result
    
a = Solution()
print(a.productExceptSelf([2,3,4,5]))
