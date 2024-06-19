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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int)->list:
    # ***Esta copia deja referencia
    # new_sudoku=[[99]*len(sudoku)]*len(sudoku)
    # *** Esta copia deja referencia
    # new_sudoku=[i for i in sudoku]
    # *** Esta copia deja referencia
    # new_sudoku=[]
    # for member in sudoku:
    # new_sudoku.append(member)
    new_sudoku=[]
    for row in range(len(sudoku)):
        new_sudoku.append([])
        for col in range(len(sudoku)):
            new_sudoku[row].append(99)

    for row in range(0,len(sudoku)):
        for column in range(len(sudoku)):
            new_sudoku[row][column]=sudoku[row][column]

    new_sudoku[row_no][column_no] = number
    return new_sudoku

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
    # sudoku  = [
    # [0, 1, 2, 3, 4, 5, 6, 6, 8],
    # [10, 11, 12, 13, 14, 15, 16, 17, 18],
    # [20, 21, 22, 23, 24, 25, 26, 27, 28],
    # [30, 31, 32, 33, 34, 35, 36, 37, 38],
    # [40, 41, 42, 43, 44, 45, 46, 47, 48],
    # [50, 51, 52, 53, 54, 55, 56, 57, 58],
    # [60, 61, 62, 63, 64, 65, 66, 67, 68],
    # [70, 71, 72, 73, 74, 75, 76, 77, 78],
    # [80, 81, 82, 83, 84, 85, 86, 87, 88]
    # ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)