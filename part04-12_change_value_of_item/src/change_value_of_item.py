# Write your solution here
my_List = [1, 2, 3, 4, 5]
index = 0
while True:
    index = int(input("Index:"))
    if index == -1:
        break
    new_Value = int(input("New value:"))
    my_List[index] = new_Value
    print(my_List)