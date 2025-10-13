class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using hashmap
        last_seen_index = {}
        for i, value in enumerate(nums):
            if value in last_seen_index:
                prev_index = last_seen_index[value]
                if i - prev_index <= k:
                    return True
            last_seen_index[value] = i
        return False 

       
        