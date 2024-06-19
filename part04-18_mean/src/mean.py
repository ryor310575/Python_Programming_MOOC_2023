# Write your solution here
# Write your solution here
def length(items: list)->int:
    return len(items)
def mean(my_list: list) -> str:
    list_length = length(my_list)
    list_sum=sum(my_list)
    list_mean=list_sum/list_length
    return list_mean
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)