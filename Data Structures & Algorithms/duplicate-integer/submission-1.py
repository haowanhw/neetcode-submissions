class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ind = 0
        if len(nums) < 2:
            return False
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                return True
            else:
                ind = ind + 1
        return False
