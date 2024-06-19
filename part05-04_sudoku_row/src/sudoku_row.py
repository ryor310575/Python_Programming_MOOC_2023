# Write your solution here
# def row_correct(sudoku: list, row_no: int)-> bool:
#     good_row = True
#     counter_number=0
#     for col in sudoku[row_no]:
#         for sk_number in range(1,10):
#             if col==sk_number:
#                 counter_number +=1
#     if counter_number != 9:
#         good_row = False
#     return good_row
def row_correct(sudoku: list, row_no: int)-> bool:
    good_row = True
    counter_number=0
    for sk_number in range(1,10):
        if sudoku[row_no].count(sk_number)>1:
            good_row = False
    return good_row

if __name__ == "__main__":
    sudoku = [
    [9, 7, 6, 0, 8, 4, 3, 2, 1],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))