# Write your solution here
phone_book={}
while True:
    command=int(input("command (1 search, 2 add, 3 quit): "))
    # Salir
    if command == 3:
        print("quitting...")
        break
    # Buscar
    elif command==1:
        name=input("name: ")
        if name in phone_book:
            for tlf in phone_book[name]:
                print(tlf)
        else:
            print("no number")
    # Agregar
    elif command==2:
        name=input("name: ")
        number=input("number: ")
        if name not in phone_book:
            phone_book[name]=[]
        phone_book[name].append(number)
        print("ok!")
    else:
        print("Wrong Selection")