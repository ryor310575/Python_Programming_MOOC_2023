# Copy here code of line function from previous exercise
def line(times,char):
    i = 0
    if char == "":
        char = "*"
    line = ""
    while i < times or len(line) < times:
        line = line + char[0]
        i += 1
    print(line)



def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, "#")
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
