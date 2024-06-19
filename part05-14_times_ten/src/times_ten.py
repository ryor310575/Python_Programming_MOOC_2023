# Write your solution here
def times_ten(start_index: int, end_index: int)-> dict:
    dictionary={}
    counter=start_index
    while counter <= end_index:
        dictionary[counter]=counter * 10
        counter += 1
    return dictionary


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)