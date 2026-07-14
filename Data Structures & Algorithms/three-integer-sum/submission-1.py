class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            l = x+1
            r = len(nums)-1
            target = 0-nums[x]
            while l < r :
                s = nums[l] + nums[r]
                if s == target:
                    result.append([nums[x],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return result