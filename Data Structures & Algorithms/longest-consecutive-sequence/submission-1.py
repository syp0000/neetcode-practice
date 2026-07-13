class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for x in seen:
            if x-1 not in seen:
                c_length = 1
                c_num = x
                while c_num + 1 in seen:
                    c_length += 1
                    c_num += 1
                longest = max(longest,c_length)
        return longest

"""
Create a set from nums
Initialize longest to 0

For each number x in the set:
    If x - 1 is not in the set:
        Initialize current length to 1
        Initialize current number to x

        While current number + 1 is in the set:
            Increment current length by 1
            Increment current number by 1

        Update longest with max(longest, current length)

Return longest
"""
