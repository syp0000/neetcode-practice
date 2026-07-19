class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows*cols) - 1
        while low <= high:
            mid = (low+high)//2
            row = mid//cols
            col = mid%cols
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        