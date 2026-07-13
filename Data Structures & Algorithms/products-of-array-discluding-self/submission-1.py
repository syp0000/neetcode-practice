class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        l_product = 1
        r_product = 1
        for i in range(len(nums)):
            ans[i] = l_product
            l_product *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*= r_product
            r_product *= nums[i]
        return ans
        