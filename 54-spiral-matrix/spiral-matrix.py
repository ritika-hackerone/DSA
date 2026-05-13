class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # boundaries
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        arr = []
        while top <= bottom and left <= right:
            # left to right
            for i in range(left, right + 1):
                arr.append(matrix[top][i])
            top += 1
            # top to bottom
            for i in range(top, bottom + 1):
                arr.append(matrix[i][right])
            right -= 1
            # right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    arr.append(matrix[bottom][i])
                bottom -= 1
            # bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    arr.append(matrix[i][left])
                left += 1
        return arr






        