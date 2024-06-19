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
def read_fruits()->dict:
    fruits_dict={}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits_dict[parts[0]]=float(parts[1])
    return fruits_dict
if __name__ == "__main__":
    print(read_fruits())
