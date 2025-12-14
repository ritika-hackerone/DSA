class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique = len(set(candyType))
        return int(min((len(candyType))/2, unique))


        