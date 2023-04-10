class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if the list is empty, return 0
        if len(nums) == 0:
            return 0
        # sort the list
        nums.sort()
        
        longest_sequence = 1
        maximum = -1
        # iterate through the list
        for i in range(len(nums) - 1):
            # if the next number is one more than the current number, increment the longest sequence
            if nums[i] + 1 == nums[i + 1]:
                longest_sequence += 1
                # if the longest sequence is greater than the maximum, set the maximum to the longest sequence
                if longest_sequence > maximum:
                    maximum = longest_sequence
            # if the next number is the same as the current number, continue
            elif nums[i] == nums[i + 1]:
                continue
            # if the next number is not one more than the current number, reset the longest sequence
            else:
                longest_sequence = 1
        # if the longest sequence is greater than the maximum, set the maximum to the longest sequence
        if longest_sequence > maximum:
            maximum = longest_sequence
        
        return maximum