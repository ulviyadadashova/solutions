class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(i, j, board, [[False] * len(row) for row in board], word):
                    return True
        return False
    def search(self, i, j, board, marked, word):
        if word == "":
            return True
        if not(i >= 0 and i < len(board) and j >= 0 and j < len(board[0])):
            return False
        if not marked[i][j] and board[i][j] == word[0]:
            marked[i][j] = True
            ret = (
                self.search(i + 1, j, board, marked, word[1:]) or
                self.search(i - 1, j, board, marked, word[1:]) or
                self.search(i, j + 1, board, marked, word[1:]) or
                self.search(i, j - 1, board, marked, word[1:])
            )
            if ret:
                return True
            marked[i][j] = False
        return False
        