from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = deque()
        water = []
        max_l = 0
        max_r = 0
        for i in range(len(height)):
            max_l = max(height[i], max_l)
            left_max.append(max_l)
        for i in range(len(height)-1, -1,-1):
            max_r = max(height[i], max_r)
            right_max.appendleft(max_r)
        for i in range(len(height)):
            water.append(min(left_max[i], right_max[i])-height[i])
        print(right_max)
        print(left_max)
        print(water)
        print(height)
        return sum(water)
            

"""
initialize left_max as list
initialize right_max as list
initialize water as list
initialize max_l as 0
initialize max_r as 0
loop from 0 to index i:
    max_l = max(height[i], max_l)
    left_max[i].add(max_l)
loop from i as len(height)-1 to index 0:
    max_r = max(height[i], max_r)
    right_max[i].add(max_r)
loop from 0 to index i:
    water[i] = min(left_max[i], right_max[i])-height[i]

return sum(water)
"""