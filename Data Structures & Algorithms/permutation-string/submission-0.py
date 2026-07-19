class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i, 0)
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            count_s2 = {}
            for i in s2[l:r+1]:
                count_s2[i] = 1 + count_s2.get(i, 0)
            if count_s2 == count:
                return True
            l += 1
            r += 1

        return False


        