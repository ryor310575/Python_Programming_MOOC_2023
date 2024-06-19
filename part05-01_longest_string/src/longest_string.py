# Write your solution here
def longest(my_list:list)->str:
    lenght_list=[]
    for word in my_list:
        lenght_list.append(len(word))
    # max_length=max(lenght_list)
    # longest_word_positon=lenght_list.index(max(lenght_list))
    longest_word=my_list[lenght_list.index(max(lenght_list))]
    return longest_word

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))