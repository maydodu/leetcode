class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            if counts.get(target - nums[i], 0) != 0 and i != nums.index(target - nums[i]):
                return i, nums.index(target - nums[i])