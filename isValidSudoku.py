class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashr=defaultdict(set)
        hashc=defaultdict(set)
        hash33=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in hashr[i] or board[i][j] in hashc[j] or board[i][j] in hash33[str(i//3)+str(j//3)]:
                    return False
                # row
                hashr[i].add(board[i][j])
                # column
                hashc[j].add(board[i][j])
                # check 3 by 3 grid
                hash33[str(i//3)+str(j//3)].add(board[i][j])

        return True
