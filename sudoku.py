from itertools import chain


def done_or_not(board):
    if not (all([len(set(row)) == 9 for row in board])
            and all([len(set(column)) == 9 for column in [[board[j][i] for j in range(9)] for i in range(9)]])):
        return 'Try again!'
    for vertical_row_number in range(3):
        for horizontal_row_number in range(3):
            if len(set(list(
                    chain(*[region_row[horizontal_row_number * 3: (horizontal_row_number + 1) * 3] for region_row in
                            board[vertical_row_number * 3: (vertical_row_number + 1) * 3]])))) != 9:
                return 'Try again!'
    return 'Finished!'
