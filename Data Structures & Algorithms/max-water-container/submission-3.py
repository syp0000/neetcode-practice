class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights)-1
        if len(heights) == 2:
            max_area = min(heights[l], heights[r]) * (r-l)
        while l < r:
            max_area = max(max_area,min(heights[l], heights[r]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
                max_area = max(max_area,min(heights[l], heights[r]) * (r-l))
                
            elif heights[r] > heights[l]:
                l += 1
                max_area = max(max_area,min(heights[l], heights[r]) * (r-l))
                
            else:
                r -= 1
                l += 1
                max_area = max(max_area,min(heights[l], heights[r]) * (r-l))
                print(max_area)
        return max_area
            