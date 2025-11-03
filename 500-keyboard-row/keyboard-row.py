class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            lower = set(word.lower())
            if lower <= row1 or lower <= row2 or lower <= row3:
                res.append(word)
        return res
       
        