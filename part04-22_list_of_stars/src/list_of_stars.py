# Write your solution here
def list_of_stars(lista : list):
    for numero in lista:
        cadena = "*" * numero
        print(cadena)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])