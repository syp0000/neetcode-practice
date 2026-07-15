class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights)-1
        while l < r:
            max_area = max(max_area,min(heights[l], heights[r]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
                l += 1
        return max_area
            