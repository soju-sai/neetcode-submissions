class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchRow(m):
            top, bot = 0, len(m)-1
            while top <= bot:
                mid = (top + bot) // 2
                if target > m[mid][-1]:
                    top = mid + 1
                elif target < m[mid][0]:
                    bot = mid - 1
                else:
                    # Target is within this row's range
                    return mid

            return -1

        def searchCol(tr):
            if tr == -1:
                return False

            l, r = 0, len(tr)-1
            while l <= r:
                mid = (l + r) // 2
                midVal = tr[mid]
                if target < midVal:
                    r = mid - 1
                elif target > midVal:
                    l = mid + 1
                else:
                    return True

            return False

        targetRow = searchRow(matrix)
        print(targetRow)

        return searchCol(matrix[targetRow])