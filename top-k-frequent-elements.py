class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = count.get(number, 0) + 1

        for num, cnt in count.items():
            frequencies[cnt].append(num)

        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if(len(res) == k):
                    return res