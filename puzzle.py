"""
GitHub link
"""


def horizontal_check(board: list) -> bool:
    """
    Check the uniqueness of the digits in the rows.
    Return True if every digit is unique and False if not.

    >>> horizontal_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> horizontal_check(["**** ****", "***111***", "**  3****", "* 4 1****", "     9 5 ",
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    pass


def rotate_board_to_vertical(board: list) -> list:
    """
    Rotate board in the way that its columns become the rows.
    Return new board as a list.

    >>> rotate_board_to_vertical(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",
                                  " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ', '  31 81  ', '****93 2*', '****   **',\
 '****5 ***', '**** ****']
    """
    pass


def vertical_check(board: list) -> bool:
    """
    Check the uniquness of the digits in the columns.
    Return True if every digit is unique and False if not.

    >>> horizontal_check(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> horizontal_check(["**** ****", "***9 ****", "**  3****", "* 4 1****", "     9 5 ",
                          " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    pass


def coloured_check(board: list) -> bool:
    """
    Check the uniquness of the digits in every same-coloured cell.
    Return True if every digit is unique and False if not.

    >>> coloured_check(["****1****", "*** 2****", "**  3****", "*   4****", "    56781",
           "        *", "2      **", "      ***", "3 4  ****"])
    False
    >>> coloured_check(["**** ****", "*** 2****", "**  3****", "*   4****", "    56781",
           "        *", "2      **", "      ***", "3 4  ****"])
    True
    """
    pass


def validate_board(board: list) -> bool:
    """
    Check if the board suites the game rules.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",
                        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***9 ****", "**  3****", "* 4 1****", "     9 5 ",
                        " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True

    >>> validate_board(["****1****", "*** 2****", "**  3****", "*   4****", "    56781",
           "        *", "2      **", "      ***", "3 4  ****"])
    False
    >>> validate_board(["**** ****", "*** 2****", "**  3****", "*   4****", "    56781",
           "        *", "2      **", "      ***", "3 4  ****"])
    True
    """
    pass
