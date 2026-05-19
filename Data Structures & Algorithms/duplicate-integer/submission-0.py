class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ind = 0
        if len(nums) < 2:
            return False
        for num in range(len(nums) - 1):
            if nums[ind + 1] == nums[ind]:
                return True
            else:
                ind = ind + 1
        return False
