class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i
        
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in indices and i != indices[residual]:
                return [i, indices[residual]]