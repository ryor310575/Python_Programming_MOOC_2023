# Write your solution here
def no_vowels(my_string: str)->str:
    string_no_vowels = ""
    string_vowels = ["a","e","i","o","u"]
    for character in my_string:
        character = character.lower()
        if character not in string_vowels:
            string_no_vowels = string_no_vowels + character
    return string_no_vowels

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))