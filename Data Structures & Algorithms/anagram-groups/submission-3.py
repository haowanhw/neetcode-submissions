class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        dic = {}

        for i in strs:
            chars = tuple(sorted(i))
            dic[chars] = []

        for i in strs:
            dic[tuple(sorted(i))].append(i) 
        
        return list(dic.values())

        

        