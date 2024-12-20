# Please write a function named squared, which takes a string argument
# and an integer argument, and prints out a square of characters as
# specified by the examples below.
#
# squared("ab", 3)
# aba
# bab
# aba
# print()
# squared("aybabtu", 5)
# aybab
# tuayb
# abtua
# ybabt
# uayba
def squared(word:str, side:int):
    high=0
    memory=0
    while high<side:
        width=0
        to_print = ""
        while width<side:
            if memory > len(word) - 1:
                memory = 0
            to_print= to_print + word[memory]
            memory+=1
            width+=1
        print(to_print)
        high+=1
squared("ab", 3)
print()
squared("aybabtu", 5)