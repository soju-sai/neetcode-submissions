class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        def dfs(preRow, preLv):
            if preLv == numRows:
                return

            curRow = []
            i, j = 0, 1
            base = [0] + preRow + [0]
            while j < len(base):
                curRow.append(base[i] + base[j])
                i += 1
                j += 1
            result.append(curRow)
            
            dfs(curRow, preLv + 1)

        result.append([1])
        dfs([1], 1)

        return result

    def generate_v1(self, numRows: int) -> List[List[int]]:
        trgl = []
        for row in range(numRows):
            if row == 0:
                trgl.append([1])
            elif row == 1:
                trgl.append([1, 1])
            else:
                tmp = [None] * (row+1)
                for i in range(row + 1):
                    if i == 0 or i == row:
                        tmp[i] = 1
                    else:
                        tmp[i] = trgl[row-1][i-1] + trgl[row-1][i]
                trgl.append(tmp)
        return trgl