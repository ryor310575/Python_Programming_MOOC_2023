# Write your solution here
# name = "Mark"
# age = 37
# print("Hi " + name + " your age is " + str(age) + " years" )
# print("Hi", name, "your age is", age, "years" )
# print("Hi", name, "your age is", age, "years", sep="")
# print("Hi", name, "your age is", age, "years", sep="\n")
# print("Hi ", end="")
# print("there!")

def formatted(my_list : list) -> list:
    new_list = []
    for number in my_list:
        new_list.append(f'{number:.2f}')
    return new_list


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)