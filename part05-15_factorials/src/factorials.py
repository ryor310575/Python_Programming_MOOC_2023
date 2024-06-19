# Write your solution here
def factorials(n: int)->dict:
    dictionary={}
    factorial=1
    for number in range(1,n+1,1):
        if n == 0:
            factorial = 1
            break
        else:
            factorial=factorial * number
            dictionary[number]=factorial
    return dictionary

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
