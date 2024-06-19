# Write your solution here
def list_sum(a : list, b : list) -> list:
    suma = []
    for num1, num2 in zip(a, b):
        suma.append(num1+num2)
    return suma

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]