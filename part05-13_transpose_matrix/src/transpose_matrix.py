# Write your solution here
def transpose(matrix: list):
    new_matrix=[[99] * len(matrix)] * len(matrix[0])
    rows=len(matrix)
    cols=len(matrix[0])
    raw_value=0
    col_value=0
    count_row=0
    count_col=0
    while count_row<rows:
        count_col=count_row
        while count_col<cols:
            raw_value=matrix[count_row][count_col]
            col_value=matrix[count_col][count_row]
            matrix[count_col][count_row]=raw_value
            matrix[count_row][count_col]=col_value
            count_col+=1
        count_row+=1

if __name__ == "__main__":
    my_matrix=[[0,1,2],
               [10,11,12],
               [20,21,22]]
    print(my_matrix)
    transpose(my_matrix)
    print(my_matrix)