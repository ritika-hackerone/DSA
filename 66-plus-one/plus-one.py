class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # range (starting pt. , stopping  pt, steps(dec i by 1))
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: # if element is [9], 9 + 1 --> [,0]
                digits[i] = 0
            if i == 0: # [1] + [ _ , 0 ] ---> [1,0]
                return [1] + digits
        