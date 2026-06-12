class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for idx, num in enumerate(nums):
            if num == 0:
                for i in nums[idx + 1 : ]:
                    if i == 0:
                        return [0] * len(nums)
        
        total = 1
        for num in nums:
            if num != 0:
                total = total * num
        if 0 in nums:
            for num in nums:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(int(total / num))
        
        return res
        