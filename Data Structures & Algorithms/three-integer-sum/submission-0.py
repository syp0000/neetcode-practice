class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for x in range(len(nums)):
            l = x+1
            r = len(nums)-1
            target = 0-nums[x]
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    result.add((nums[x],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return [list(t) for t in result]