class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while(start_index <= end_index):
            mid_index = (start_index + end_index) // 2
            if target > nums[mid_index]:
                start_index = mid_index + 1

            elif target < nums[mid_index]:
                end_index = mid_index - 1
            
            else:
                return mid_index

        return -1