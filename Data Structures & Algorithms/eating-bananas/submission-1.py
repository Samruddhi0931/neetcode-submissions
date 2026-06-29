class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1              # slowest possible speed
        right = max(piles)     # fastest needed (finish biggest pile in 1hr)

        while left < right:    # find leftmost valid speed
            mid   = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)

            if hours <= h:
                right = mid    # speed works! try slower
            else:
                left = mid + 1 # too slow, need faster

        return left