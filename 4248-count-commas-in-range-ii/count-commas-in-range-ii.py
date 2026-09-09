class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        threshold = 1000 # threshold means starting point

        while threshold <= n:
            ans += n - threshold + 1 #Main calculation
            threshold *= 1000   # Ye threshold ko next comma level par le jaata hai just example 1000 × 1000 = 1,000,000
        return ans
        