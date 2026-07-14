class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []

        for i, h in enumerate(heights):
            for j in range(i, len(heights)):
                area = (j - i) * min(h, heights[j])
                areas.append(area)

        return max(areas)
        