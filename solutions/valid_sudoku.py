import collections


def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    digits_row_dict = collections.defaultdict(set)
    digits_col_dict = collections.defaultdict(set)
    digits_square_dict = collections.defaultdict(set)
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            elif board[row][col] in digits_row_dict[row] \
                    or board[row][col] in digits_col_dict[col] \
                    or board[row][col] in digits_square_dict[(row // 3, col // 3)]:
                return False
            else:
                digits_row_dict[row].add(board[row][col])
                digits_col_dict[col].add(board[row][col])
                digits_square_dict[(row // 3, col // 3)].add(board[row][col])
    return True
