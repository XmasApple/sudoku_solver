import numpy as np


def get_row(table: list, row_number):
    return table[row_number]


def get_col(table: list, col_number):
    return [x[col_number] for x in table]


def get_nine(table: list, number):
    return [table[number // 3 * 3 + x // 3][number % 3 * 3 + x % 3] for x in range(9)]


def get_nine_number_of(row, col):
    return row // 3 * 3 + col // 3


def get_nine_of(table: list, row, col):
    return get_nine(table, get_nine_number_of(row, col))


def is_zeros_in_table(table: list):
    for row in table:
        for elem in row:
            if elem == 0:
                return True
    return False


def main():
    table = [[9, 0, 8, 0, 5, 6, 0, 0, 4],
             [0, 0, 0, 8, 0, 0, 0, 0, 2],
             [7, 0, 3, 9, 0, 0, 0, 0, 5],

             [0, 0, 2, 0, 0, 8, 3, 0, 0],
             [8, 0, 0, 7, 0, 0, 0, 0, 9],
             [5, 4, 0, 0, 6, 1, 0, 0, 0],

             [1, 5, 0, 0, 8, 0, 0, 4, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 8],
             [0, 0, 0, 0, 0, 0, 5, 7, 3]]

    while is_zeros_in_table(table):
        for row in range(9):
            for col in range(9):
                if table[row][col] == 0:
                    predictions = []
                    for prediction in range(1, 10):
                        if (
                                prediction not in get_row(table, row) and
                                prediction not in get_col(table, col) and
                                prediction not in get_nine_of(table, row, col)):
                            predictions.append(prediction)
                    if len(predictions) == 1:
                        table[row][col] = predictions[0]

        print(np.array(table))


if __name__ == '__main__':
    main()
