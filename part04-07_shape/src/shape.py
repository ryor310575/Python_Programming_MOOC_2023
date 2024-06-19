# Copy here code of line function from previous exercise and use it in your solution
def line(times,char):
    i = 0
    if char == "":
        char = "*"
    line = ""
    while i < times or len(line) < times:
        line = line + char[0]
        i += 1
    print(line)
# Square
def rectanle(w_size,h_size, character):
    # You should call function line here with proper parameters
    i = 1
    while i <= h_size:
        line(w_size, character)
        i += 1

# Triangle
def triangle(size,character):
    i=1
    while i <= size:
        line(i,character)
        i+=1

def shape(t_size, t_symbol, s_size, s_symbol):
    triangle(t_size,t_symbol)
    rectanle(t_size,s_size, s_symbol)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(10, "@", 6, "!")