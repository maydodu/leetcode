class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        res = []
        # sort nums to make it easier to check for duplicates
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in res:
                            res.append([nums[i], nums[j], nums[k]])

        return res