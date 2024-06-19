# Write your solution here
# This exercise is about creating a program which allows the user to search for 
# recipes based on their names, preparation times, or ingredients used. 
# The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name 
# of the recipe, the second line contains an integer number representing the 
# preparation time in minutes, and the remaining line or lines contain the ingredients used, 
# one on each line. The recipe ends with an empty line, with the exception of the final 
# recipe in the file which just ends with the end of the file. So, 
# there can be more than one recipe in a single file, like in the example below.
# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter
###################

#*******************************************************
#*********  Convertir un archivo a lista  ********
# Esta funcion convierte un archivo con palabras en cada linea
#*******************************************************
def file_to_list(fle_name:str)->list:
    file_info = [] #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            # Evaluamos si los argimentos son numeros y los evaluamos como numeros si son cadenas los evaluamos como cadenas
            try:
                file_info.append(int(line.strip()))
            except:
                file_info.append(line.strip())
    file_info.append('') # Agrega un caracter de final de archivo a la lista
    return file_info
#*******************************************************
#*****  Convertir un archivo a Lista de listas  ********
#*******************************************************
def slice_list(general_list:list)->list:
    list_of_list=[]
    individual_list=[]
    item_counter=0
    # Create a list of recipes
    while item_counter < len(general_list):
        if general_list[item_counter] == '':
            temp_list=individual_list.copy()
            list_of_list.append(temp_list)
            individual_list.clear()
        else:
            individual_list.append(general_list[item_counter])
        item_counter +=1
    return list_of_list

#*******************************************************
#*********  Convertir un archivo a diccionario  ********
#*******************************************************
def file_to_dict(file_name:str)->dict:
    file_list=file_to_list(file_name)
    list_of_list=slice_list(file_list)
    file_dict = {} #Abre un diccionario vacio
    for recipe in list_of_list:
        file_dict[recipe[0]]=recipe[1:]
    return file_dict

#*******************************************************
#*********       recipes based on the name      ********
# Search for recipes based on the name of the recipe
# Please write a function named search_by_name(filename: str, word: str), 
# which takes a filename and a search string as its arguments. 
# he function should go through the file and select all recipes whose name 
# contains the given search string. The names of these recipes are then returned in a list.
#*******************************************************
def search_by_name(filename: str, word: str) -> list:
    file_dict=file_to_dict(filename)
    recipe_names=[]
    for recipes in file_dict.keys():
        if word.lower() in str(recipes).lower():
            recipe_names.append(recipes)
    return recipe_names
#*******************************************************
#*********       recipes based on the time      ********
# Please write a function named search_by_time(filename: str, 
# prep_time: int), which takes a filename and an integer as its arguments. 
# The function should go through the file and select all 
# recipes whose preparation time is at most the number given. 
# The names of these recipes are again returned in a list, 
# but the preparation time should be appended to each name. 
#*******************************************************
def search_by_time(filename: str, prep_time: int) -> list:
    file_dict=file_to_dict(filename)
    recipe_names=[]
    recipe_names=[]
    position_counter=0
    for recipe,ingredients in file_dict.items():
        if prep_time >= ingredients[0]:
            recipe_names.append(f'{recipe}, preparation time {ingredients[0]} min')
        position_counter +=1
    return recipe_names

#*******************************************************
#*********   recipes based on the ingredient    ********
# Please write a function named search_by_ingredient(filename: str, ingredient: str), 
# which takes a filename and a search string as its arguments. The function should 
# go through the file and select all recipes whose ingredients contain the given search string.
# The names of these recipes are returned in a list just like in the second part, 
# with the preparation time appended. Please have a look at the example below.
# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min
#*******************************************************
def search_by_ingredient(filename: str, ingredient: str) -> list:
    file_dict=file_to_dict(filename)
    recipe_names=[]
    for recipes, ingredients in file_dict.items():
        if ingredient in ingredients:
            recipe_names.append(f'{recipes}, preparation time {ingredients[0]} min')
    return recipe_names

# You can test your function by calling it within the following block
if __name__ == "__main__":
    found_recipes = search_by_name("recipes2.txt", "oat")
    #print("-----------   search_by_name recipes2.txt oat")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_name("recipes2.txt", "fish")
    #print("-----------   search_by_name recipes2.txt fish")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_name("recipes1.txt", "Cake")
    #print("-----------   search_by_name recipes2.txt Cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 15)
    #print("-----------   search_by_time recipes1.txt 15")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    #print("-----------   search_by_time recipes1.txt 20")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    #print ("-----------   search_by_ingredient recipes1.txt eggs")
    for recipe in found_recipes:
        print(recipe)

# FAIL:
# RecipeSearchPart1Test: test_3_search_by_name_1
# 1 != 2 : Function returns a wrong number of recipes when called with 
# search_by_name("recipes2.txt", "oat")
# FAIL:
# RecipeSearchPart2Test: test_6_search_by_time_1
# 1 != 0 : Function returns a wrong number of recipes when called with 
# search_by_time("recipes1.txt", 20)
# FAIL:
# RecipeSearchPart3Test: test_9_search_by_ingredient_1
# 1 != 0 : Function returns a wrong number of recipes when called with 
# search_by_ingredient("recipes2.txt", "fish")