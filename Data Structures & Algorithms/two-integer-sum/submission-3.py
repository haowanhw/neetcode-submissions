class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in nums:
                for j in range(len(nums)):
                    if nums[j] == residual and i != j:
                        return [i, j]