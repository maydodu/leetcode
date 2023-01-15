class Solution:  
    def containsDuplicate(self, nums: List[int]) -> bool: 
        counts = {}  # key: number, value: count
        for i in nums:  # O(n)
            if counts.get(i) != None:  # O(1)
                counts[i] += 1
                if counts[i] == 2:  
                    return True  
            else:  # O(1)
                counts[i] = 1

        return False
