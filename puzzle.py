"""
GitHub link: https://github.com/alorthius/lab1_puzzle
"""


def horizontal_check(board: list) -> bool:
    """
    Check the uniqueness of the digits in the rows.
    Return True if every digit is unique and False if not.

    >>> horizontal_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> horizontal_check(["**** ****", "***111***", "**  3****", "* 4 1****", "     9 5 ",\
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for row in board:
        digits = row.replace('*', '')
        digits = digits.replace(' ', '')

        # there are the same digits in one row or not a single one
        if len(digits) != len(set(digits)):
            return False

    return True


def rotate_board_to_vertical(board: list) -> list:
    """
    Rotate board in the way that its columns become the rows.
    Return new board as a list.

    >>> rotate_board_to_vertical(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
                                  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ', '  31 81  ', '****93 2*', '****   **',\
 '****5 ***', '**** ****']
    """
    index = 0
    new_board = []

    while index != len(board):
        new_row = ''

        for row in board:
            new_row += row[index]
        new_board.append(new_row)
        index += 1

    return new_board


def vertical_check(board: list) -> bool:
    """
    Check the uniquness of the digits in the columns.
    Return True if every digit is unique and False if not.

    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> vertical_check(["**** ****", "***1 ****", "**  3****", "* 4 9****", "     9 5 ",\
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    return horizontal_check(rotate_board_to_vertical(board))


def one_coloured_cells(board: list) -> list:
    """
    """
    same_coloured_sells = []
    index = 0
    column_index = len(board) - 1

    while index != len(board) - 4:
        row_1 = ''
        row_2 = ''

        for row in board[:column_index]:
            row_1 += row[index]
        row_2 += board[column_index][len(board) - column_index - 1:]
        new_row = row_1 + row_2
        same_coloured_sells.append(new_row)
        index += 1
        column_index -= 1

    return same_coloured_sells


def coloured_check(board: list) -> bool:
    """
    Check the uniquness of the digits in every same-coloured cell.
    Return True if every digit is unique and False if not.

    >>> coloured_check(["****1****", "*** 2****", "**  3****", "*   4****", "    56781",\
           "        *", "2      **", "      ***", "3 4  ****"])
    False
    >>> coloured_check(["**** ****", "*** 2****", "**  3****", "*   4****", "    56781",\
           "        *", "2      **", "      ***", "3 4  ****"])
    True
    """
    return horizontal_check(one_coloured_cells(board))


def validate_board(board: list) -> bool:
    """
    Check if the board suites the game rules.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
                        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 7****", "     9 5 ",\
                        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True

    >>> validate_board(["****1****", "*** 2****", "**  3****", "*   4****", "    56781",\
           "        *", "2      **", "      ***", "3 4  ****"])
    False
    >>> validate_board(["**** ****", "*** 2****", "**  3****", "*   4****", "    56781",\
           "        *", "2      **", "      ***", "3 4  ****"])
    True
    """
    if (not horizontal_check(board) or not horizontal_check(rotate_board_to_vertical(board))
            or not coloured_check(board)):
        return False
    return True
