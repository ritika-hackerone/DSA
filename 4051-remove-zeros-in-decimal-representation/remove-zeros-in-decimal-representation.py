class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n) # TC = O(log n)
        s_remove_0 = s.replace('0','')
        return int(s_remove_0)
