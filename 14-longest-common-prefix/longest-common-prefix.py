class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # using sort method
        strs.sort()
        first = strs[0]
        last = strs[-1]
        min_val = min(len(first), len(last))
        for i in range(min_val):
            if last[i] != first[i]:
                return last[:i]
        return last[: min_val]
        