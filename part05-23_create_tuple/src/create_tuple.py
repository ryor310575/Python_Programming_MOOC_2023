# Write your solution here
def sum_list(my_list:list)->list:
    summatory=0
    for number in my_list:
        summatory=summatory+number
    return summatory

def create_tuple(x: int, y: int, z: int) -> tuple:
    new_tuple=()
    temp_list=[]
    temp_list.append(x)
    temp_list.append(y)
    temp_list.append(z)
    temp_list.sort()
    new_tuple=(min(temp_list),max(temp_list),sum_list(temp_list))

    return new_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))