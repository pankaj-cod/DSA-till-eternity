
class Solution:
    def minRotations(self, s: str) -> int:
        rots = 0
        dial = 0

        for ch in s:
            num = int(ch)

            diff = abs(dial - num)
            rots += min(diff, 10 - diff)

            dial = num

        return rots
