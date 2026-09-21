class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_dict = defaultdict(int)
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)

        # Row and Column Checks
        for row in range(9):
            for col in range(9):
                row_dict[board[row][col]] += 1
                col_dict[board[col][row]] += 1
                if row_dict[board[row][col]] > 1 and board[row][col] != ".":
                    print(f"Row {row} has {board[row][col]} twice")
                    return False
                if col_dict[board[col][row]] > 1 and board[col][row] != ".":
                    print(f"Col {col} has {board[col][row]} twice")
                    return False
            row_dict = defaultdict(int)
            col_dict = defaultdict(int)

        # Box Checks
        row_offset = 0
        col_offset = 0
        for box in range(9):
            for row in range(row_offset,row_offset + 3):
                for col in range(col_offset, col_offset + 3):
                    box_dict[board[row][col]] += 1
                    if box_dict[board[row][col]] > 1 and board[row][col] != ".":
                        print(f"Box {box} has {board[row][col]} twice")
                        return False
            box_dict = defaultdict(int)
            row_offset += 3
            if col_offset >= 6:
                break
            if col_offset > 0:
                col_offset += 3
            if row_offset >= 6:
                row_offset = 0
                col_offset += 3

        return True
                

