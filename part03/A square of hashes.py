# Please write a function named hash_square(length), which takes an integer argument.
# The function prints out a square of hash characters, and the argument specifies the
# length of the side of the square.
#
# hash_square(3)
# print()
# hash_square(5)
# ###
# ###
# ###
#
# #####
# #####
# #####
# #####
# #####
def hash_square(side:int):
    high=0
    width=0
    to_print=""
    while high<side:
        while width<side:
            to_print=to_print +"#"
            width+=1
        print(to_print)
        high+=1
hash_square(3)
print()
hash_square(5)
