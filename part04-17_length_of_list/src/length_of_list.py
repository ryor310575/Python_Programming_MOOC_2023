# Write your solution here
def length(items: list)->int:
    return len(items)
def mean(my_list: list) -> str:
    list_length = length(my_list)
    list_sum=sum(my_list)
    list_mean=list_sum/list_length
    return f'mean value is {list_mean}'
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(result)