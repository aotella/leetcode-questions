
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                if c < 0 :
                    c = 1
                else:
                    c = -1
        return c
