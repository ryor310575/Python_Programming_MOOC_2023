# Write your solution here
def length_of_longest(my_list: list) -> int:
    lenght_list=[]
    for word in my_list:
        lenght_list.append(len(word))
    return max(lenght_list)



if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)