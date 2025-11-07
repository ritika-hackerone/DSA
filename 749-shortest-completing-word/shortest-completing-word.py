class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words=sorted(words, key=len)
        plate=Counter(i.lower() for i in licensePlate if i.isalpha())

        for i in words:
            if Counter(i)>=plate:
                return i
         
        