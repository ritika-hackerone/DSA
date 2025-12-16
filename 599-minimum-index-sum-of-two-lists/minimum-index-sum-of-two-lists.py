class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1_map = {word:val  for  val,word  in  enumerate(list1)}
        min_sum = float('inf')
        res = []
        for j, word in enumerate(list2):
            if word in l1_map:
                index_sum = j + l1_map[word]
                if index_sum < min_sum:
                    min_sum = index_sum
                    res = [word]
                elif index_sum == min_sum:
                    res.append(word)
        return res




        