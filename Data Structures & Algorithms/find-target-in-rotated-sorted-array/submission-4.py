class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return 0
        while l < r:
            mid = (l + r) //2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        min_index = l
        if target > nums[-1]:
            r = min_index - 1
            l = 0
        if target <= nums[-1]:
            l = min_index
            r = len(nums)-1
        
        while l<= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
            
