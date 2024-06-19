# Write your solution here
def no_shouting(my_list:list)->list:
    lower_list = []
    for lower_string in my_list:
        if not lower_string.isupper():
            lower_list.append(lower_string)
    return lower_list


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)