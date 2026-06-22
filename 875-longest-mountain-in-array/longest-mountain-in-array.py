class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        indx = 1
        max_len =  0
        while indx < n:
            # Count increasing step 
            up = 0
            while indx < n and arr[indx] > arr[indx-1]:
                up += 1
                indx += 1
            # Count decreasing step 
            down = 0
            while indx < n and arr[indx] < arr[indx-1]:
                down += 1
                indx += 1
            # Check if valid mountain exists
            if up>0 and down>0:
                max_len = max(max_len, up + down + 1)
            # Skip flat areas
            while indx<n and arr[indx] == arr[indx-1]:
                indx += 1
        return max_len

            

        