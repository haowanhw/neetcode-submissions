class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        idx = 0
        product = 1
        while idx != len(nums):
            for i in range(len(nums)):
                if i != idx:
                    product = product * nums[i]
            res.append(product)
            product = 1
            idx += 1
        return res

        