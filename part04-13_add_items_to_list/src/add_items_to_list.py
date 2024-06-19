# Write your solution here
my_list = []
i = 1
item_qtity = int(input("How many items:"))
while i <= item_qtity:
    item_num = int(input(f'Item {i}:'))
    my_list.append(item_num)
    i += 1
print(my_list)