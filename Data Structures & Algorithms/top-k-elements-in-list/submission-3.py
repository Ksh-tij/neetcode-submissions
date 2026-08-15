class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        
        arr = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            arr[count].append(num)
        
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res