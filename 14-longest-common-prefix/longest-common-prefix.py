class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # check if list of string is empty?
            return ""
        pref = strs[0] # initiate prefix by first string (as a reference)
        pref_len = len(pref) # set length of prefix as length of first term
        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                pref = pref[0:pref_len]
                if pref_len == 0:
                   return ""
        return pref