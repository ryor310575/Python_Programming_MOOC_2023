# Write your solution here
def first_word(a: str) -> str:
    b = a.split()
    return b[0]
def second_word(a: str) -> str:
    b = a.split()
    return b[1]
def last_word(a: str) -> str:
    b = a.split()
    return b[len(b)-1]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))