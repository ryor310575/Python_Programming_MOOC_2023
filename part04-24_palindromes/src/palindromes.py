# def palindromes(word: str):
#     for i in range(len(word)//2):
#         if word[i] != word[len(word)-i-1]:
#             return False
#     return True
 
# while True:
#     word = input("Please type in a palindrome: ")
#     if palindromes(word):
#         print(word, "is a palindrome!")
#         break
#     print("that wasn't a palindrome")
# Write your solution here
def invertir_cadena(cadena : str ):
    cadena_inv=cadena[::-1]
    #for caracter in cadena:
    #    cadena_inv= caracter + cadena_inv
    return cadena_inv

def palindromes(palin : str):
    palin_rev = invertir_cadena(palin)
    if palin == palin_rev:
        return True
    else:
        return False

def main():
        while True:
            palabra = input("Please type in a palindrome: ")
            if palindromes(palabra) == True:
                print(f'{palabra} is a palindrome!')
                break
            else:
                print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
# block!
main()