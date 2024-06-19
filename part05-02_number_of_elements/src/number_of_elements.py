# Write your solution here
def count_matching_elements(my_matrix: list, element: int)->int:
    match_counter=0
    row_lenght=len(my_matrix[0])
    col_lenght=len(my_matrix)
    col=0
    while col<col_lenght:
        row=0
        while row<row_lenght:
            if my_matrix[col][row] == element:
                match_counter+=1
            row+=1
        col+=1
    return match_counter

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))