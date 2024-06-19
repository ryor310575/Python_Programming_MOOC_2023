# Write your solution here
def remove_smallest(numbers: list):
    smallest_number = min(numbers)
    new_list=numbers.pop(numbers.index(smallest_number))
    #return new_list


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)