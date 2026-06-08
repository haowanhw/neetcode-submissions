class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for freq in range(len(bucket)-1, 0, -1):
            for i in bucket[freq]:
                res.append(i)
            if len(res) == k:
                return res