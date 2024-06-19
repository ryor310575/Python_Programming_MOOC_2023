# Write your solution here
my_list = []
i = 0
count = 0
item_word = ""
while True :
    item_word = input('Word: ')
    if item_word not in my_list:
        count +=1
    else:
        break
    my_list.append(item_word)
print(f'You typed in {count} different words')