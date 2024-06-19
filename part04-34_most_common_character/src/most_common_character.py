# Write your solution here
# __COUNT__
# my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
# print(my_string.count("o"))
# my_list = [1,2,3,1,4,5,1,6]
# print(my_list.count(1))
# __REPLACE__
# my_string = "Hi there"
# new_string = my_string.replace("Hi", "Hey")
# print(new_string)
def most_common_character(my_string:str)->int:
    list_occurrencies=[]
    max_occurrencies=0
    for characters in my_string:
        list_occurrencies.append(my_string.count(characters))
    max_occurrencies=max(list_occurrencies)
    # print(my_string[::1])
    # print(list_occurrencies)
    # print(max_occurrencies)
    # print(list_occurrencies.index(max_occurrencies))
    return my_string[list_occurrencies.index(max_occurrencies)]
#if __name__ == "__main__":
if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))