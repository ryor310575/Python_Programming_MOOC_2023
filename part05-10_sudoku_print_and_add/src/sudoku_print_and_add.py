# Write your solution here
def print_sudoku(sudoku:list):
    row_count=0
    col_count=0
    row_draw=""
    for row in sudoku:
        for column in row:
            if column == 0:
                if col_count<2:
                    row_draw=row_draw + "_ "
                else:
                    row_draw=row_draw + "_"
            else:
                if  col_count<2:
                    row_draw=row_draw + str(column) + " "
                else:
                    row_draw=row_draw + str(column)
            col_count+=1
            if col_count>2:
                row_draw=row_draw + "  "
                col_count=0
        print(row_draw)
        row_draw=""
        row_count+=1
        if row_count>2:
            print("")
            row_count=0

                
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no]=number

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)