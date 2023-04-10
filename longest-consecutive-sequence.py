aydogduwu
aydogduwu
Apr 10, 2023 23:53
Python3
Runtime313 ms
Beats
88.2%
Memory27.6 MB
Beats
97.74%
Click the distribution chart to view more details
Notes
Related Tags
0/5

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longest_sequence = 1
        maximum = -1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                longest_sequence += 1
                if longest_sequence > maximum:
                    maximum = longest_sequence
            elif nums[i] == nums[i + 1]:
                continue
            else:
                longest_sequence = 1
        if longest_sequence > maximum:
            maximum = longest_sequence
        
        return maximum