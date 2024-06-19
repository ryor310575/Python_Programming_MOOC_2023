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


def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:
        line(10, "#")
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(3)
