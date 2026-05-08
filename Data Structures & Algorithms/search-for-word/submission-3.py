class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        path = set() # 用來記錄已經走過的座標，避免重複走

        def dfs(r, c, i):
            # 確認如果已經符合全部條件，word全部跑完了，那就是回傳true
            if i == len(word):
                return True
            # 確認任何不合理的狀況，回傳False
            if ((r < 0 or c < 0 or r >= ROW or c >= COL)
                or word[i] != board[r][c]
                or (r, c) in path):
                return False
            # 以上都通過就表示目前字母符合，標註走過，並且遍歷他的四方
            path.add((r, c))
            # 遍歷目前的座標
            res = (dfs(r - 1, c, i + 1) or
                dfs(r, c -1, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c + 1, i + 1))
            # 目前的座標已確認，所以清空path，準備下一個for loop
            path.remove((r, c))
            return res

        # 遍歷整塊borad
        for r in range(ROW):
            for c in range(COL):
                # 開始進行depth first search
                res = dfs(r, c, 0)
                if res:
                    return True
        return False
