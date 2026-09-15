class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = -1

        while left <= right:
            mid = (left + right) // 2

            if self.calc(mid, piles) <= h:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best
    def calc(self, mid, piles):
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / mid)
        return hours
