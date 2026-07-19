import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        if len(piles) == h:
            return piles[-1]
        low = 1
        high = max(piles)
        hours = 0
        while low <= high:
            mid = (high+low)//2
            hours = sum(math.ceil(pile/mid) for pile in piles)
            if hours <= h:
                 high = mid -1
            elif hours > h:
                low = mid + 1
        return low

        