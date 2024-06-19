# write your solution here
# with open("/Users/ryanortega/example.txt","r") as new_file:
#     count = 0
#     total_length = 0
#     for line in new_file:
#         line = line.replace("\n", "")
#         count += 1
#         print("Line", count, line)
#         length = len(line)
#         total_length += length
# print("Total length of lines:", total_length)


# with open(""/Users/ryanortega/Library/Application Support/tmc/vscode/mooc-programming-23/part06-01_largest_number/src/numbers.txt","r") as new_file:
def largest():
    with open("numbers.txt","r") as new_file:
        count = 0
        total_length = 0
        numbers=[]
        # print(new_file.read())
        # print("===========================")
        for line in new_file:
            line = line.replace("\n", "")
            number =  int(line)
            numbers.append(number)
    return max(numbers)
if __name__ == "__main__":
    largest()


