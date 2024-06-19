# Write your solution here
# Write your solution here
def all_the_longest(my_list:list)->list:
    lenght_list=[]
    max_number=0
    longest_list=[]
    for word in my_list:
        lenght_list.append(len(word))
    max_number = max(lenght_list)
    for word in my_list:
        if len(word) == max_number:
            longest_list.append(word)
    return longest_list



if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)