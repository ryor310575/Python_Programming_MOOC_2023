# Please write a function named chessboard, which prints out a chessboard
# made out of ones and zeroes. The function takes an integer argument,
# which specifies the length of the side of the board.
# See the examples below for details:
#
#
# Sample output
# chessboard(3)
# print()
# 101
# 010
# 101
#
# chessboard(6)
# 101010
# 010101
# 101010
# 010101
# 101010
# 010101


def chessboard(side:int):
    high=0
    mem_pos=0
    mem_line=1
    while high<side:
        if mem_line==0:
            mem_line=1
        else:
            mem_line=0
        mem_pos = mem_line
        width = 0
        to_print = ""
        while width<side:
            if mem_pos==0:
                mem_pos=1
            else:
                mem_pos=0
            to_print=to_print+str(mem_pos)
            width+=1
        print(to_print)
        high+=1
chessboard(3)
print()
chessboard(6)
