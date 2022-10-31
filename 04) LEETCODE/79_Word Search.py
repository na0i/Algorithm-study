class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0] * len(board[0]) for _ in range(len(board))]
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c, word_idx, visit_check):
            nonlocal flag

            if word_idx == len(word) - 1:
                flag = True
                return

            else:
                for d in range(4):
                    next_r = r + dr[d]
                    next_c = c + dc[d]

                    if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and visit_check[next_r][
                        next_c] == 0 and word_idx < len(word) - 1 and board[next_r][next_c] == word[word_idx + 1]:
                        visit_check[next_r][next_c] = 1
                        dfs(next_r, next_c, word_idx + 1, visit_check)
                        visit_check[next_r][next_c] = 0

        flag = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if flag:
                    break

                elif board[i][j] == word[0]:
                    visited[i][j] = 1
                    dfs(i, j, 0, visited)
                    visited[i][j] = 0

        return flag