# Write your solution here
my_list = []
print("The list is now []")
i = 0
while True:
    item_action = input(f'a(d)d, (r)emove or e(x)it:')
    if item_action == "x":
        break
    elif item_action == "r":
        i -= 1
        my_list.pop(len(my_list) - 1)
        print(f'The list is now {my_list}')
    elif item_action == "d":
        i += 1
        my_list.append(i)
        print(f'The list is now {my_list}')
print("Bye!")