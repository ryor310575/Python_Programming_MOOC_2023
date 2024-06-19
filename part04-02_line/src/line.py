# Write your solution here
def line(times,char):
    i = 0
    if char == "":
        char = "*"
    line = ""
    while i < times or len(line) < times:
        line = line + char[0]
        i += 1
    print(line)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(10, "wertyui")