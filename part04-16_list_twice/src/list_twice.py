# Write your solution here
my_list = []
ordered_list=[]
i = 0
item_word = ""
while True :
    item_word = int(input('WNew item: '))
    if item_word==0:
        break
    my_list.append(item_word)
    ordered_list = sorted(my_list)
    print(f'The list now: {my_list}')
    print(f'The list in order: {ordered_list}')
print(f'Bye!')