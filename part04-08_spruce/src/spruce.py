# Write your solution here
# Copy here code of line function from previous exercise and use it in your solution
def line(times1,char1,times2,char2):
    i = 0
    if char1 == "":
        char1 = "*"
    line1 = ""
    line2 = ""
    line = ""
    while i < times1 or len(line1) < times1:
        line1 = line1 + char1[0]
        i += 1
    i=0
    while i < times2 or len(line2) < times2:
        line2 = line2 + char2[0]
        i += 1
    line=line1+line2
    print(line)

# Base
def base(w_size,character):
    pad_base= w_size - 1
    base = " " * pad_base + "*"
    print(base)

# Triangle
def triangle(size,character):
    i=1
    while i <= size:
        max_base_triangle = 2 * i - 1
        max_pad=size-i
        line(max_pad," ",max_base_triangle,character)
        i+=1
def spruce(t_size):
    print("a spruce!")
    t_symbol="*"
    triangle(t_size,t_symbol)
    base(t_size,t_symbol)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)