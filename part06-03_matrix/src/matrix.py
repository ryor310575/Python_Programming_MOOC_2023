# write your solution here
# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades = parts[1:]
#         print("Name:", name)
#         print("Grades:", grades)
#         for items in parts:
#             print(items)
def str_to_num_list(line:list)->list:
    line_list=[]
    for numbers in line:
        line_list.append(int(numbers))
    return line_list
def row_max(file:str)->list:
    row_max=[]
    with open(file) as new_file:
        for line in new_file:
            parts_str = line.split(",")
            parts_num=str_to_num_list(parts_str)
            row_max.append(max(parts_num))
    return row_max
def row_sums()->list:
    row_sum=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            parts_str = line.split(",")
            parts_num=str_to_num_list(parts_str)
            row_sum.append(sum(parts_num))
    return row_sum
def matrix_sum()->int:
    mtx_sum=sum(row_sums())
    return mtx_sum
def matrix_max()->int:
    file="matrix.txt"
    mtx_max=max(row_max(file))
    return mtx_max


if __name__ == "__main__":
    # file_name="matrix.txt"
    # print(row_sums(file_name))
    # print(matrix_sum(file_name))
    # print(matrix_max(file_name))
    # row_sums("matrix.txt")
    # matrix_sum("matrix.txt")
    # matrix_max("matrix.txt")

    row_sums()
    matrix_sum()
    matrix_max()