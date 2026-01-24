class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        hmap = {}
        max_freq = 0  # Track max frequency without recalculating
        
        for r in range(len(s)):
            # Add current character to window
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            
            # Update max frequency (O(1) instead of O(26))
            max_freq = max(max_freq, hmap[s[r]])
            
            # Calculate replacements needed
            window_size = r - l + 1
            replacements_needed = window_size - max_freq
            
            # If window is invalid, shrink from left
            if replacements_needed > k:
                hmap[s[l]] -= 1
                l += 1
            
            # Update answer (window is valid here)
            ans = max(ans, r - l + 1)
        
        return ans
        