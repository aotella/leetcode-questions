class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isInc = True
        isDec = True
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                isInc = False
            if A[i] < A[i+1]:
                isDec = False
        return isInc or isDec


