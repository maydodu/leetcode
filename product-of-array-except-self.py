class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix[i] = nums[0] * nums[1] * ... * nums[i-1]
        prefix = [1] * len(nums)
        prefix[0] = nums[0]

        # postfix[i] = nums[i+1] * nums[i+2] * ... * nums[len(nums)-1]
        postfix = [1] * len(nums)
        postfix[len(nums)-1] = nums[len(nums)-1]
        
        # calculate prefix and postfix 
        for i in range(1, len(nums), 1):
            prefix[i] = nums[i] * prefix[i-1]

        for i in range(len(nums)-2, 0, -1):
            postfix[i] = nums[i] * postfix[i+1]

        # calculate result
        result = [1] * len(nums)
        # result[i] = prefix[i-1] * postfix[i+1]
        for i in range(len(nums)):
            # if i is the first or last element, then there is no prefix or postfix
            if i == 0:
                result[i] = postfix[i+1]
            elif i == len(nums)-1:
                result[i] = prefix[i-1]
            # else there is a prefix and postfix
            else:
                result[i] = prefix[i-1] * postfix[i+1]

        return result
