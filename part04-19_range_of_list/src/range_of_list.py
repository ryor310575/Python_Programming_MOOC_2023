# Write your solution here
def range_of_list(my_list: list) -> int:
   maximun=max(my_list)
   minimun=min(my_list)
   list_range = maximun - minimun
   return list_range
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)