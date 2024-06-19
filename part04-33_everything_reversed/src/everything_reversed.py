# Write your solution here
# my_string = "exemplary"
# print(my_string[0:7:2])
# print(my_string[0:7:3])
# my_list = [1,2,3,4,5,6,7,8]
# print(my_list[6:2:-1])
# my_string = input("Please type in a string: ")
# print(my_string[::-1])
# def print_reversed(name: list):
#     # using the global variable instead of the parameter by accident
#     i = len(name_list) - 1
#     while i >= 0:
#         print(name_list[i])
#         i -= 1

# if __name__ == "__main__":
# # here the global variable is assigned
#     name_list = ["Steve", "Jean", "Katherine", "Paul"]
#     print_reversed(name_list)
#     print()
#     print_reversed(["Huey", "Dewey", "Louie"])

def everything_reversed(my_list:list)->list:
    reversed_list=[]
    reversed_word=""
    for words in my_list:
        reversed_word=words[::-1]
        reversed_list.append(reversed_word)

    return reversed_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)