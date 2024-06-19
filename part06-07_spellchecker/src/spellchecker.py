# write your solution here

#*******************************************************
#*********  Convertir un archivo a lista  ********
# Esta funcion convierte un archivo con palabras en cada linea
# en un arreglo
# 1) Toma el archivo diccionario y lo convierte en un arreglo para recorrerlo.
#*******************************************************
def file_to_list(fle_name:str)->list:
    file_info = [] #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            file_info.append(line.strip())
    return file_info


# This fiction compare tto words. The case doesnt care.
# first verify if the words have the same numbers of characters
# then verify if two words have the same characters.
# finally verify the order. If have some diference return the word
# into stars
# If everything is the same return the same word
def evaluate_words(word_to_check:str, word_right:str)-> bool:
    compare_indicator=True # Assume the words are the same
    # Set both words as lower case
    word_to_check_lower= word_to_check.lower()
    word_right_lower=word_right.lower()
    # Remove not printable characters with STRRIP Method
    word_to_check_lower= word_to_check_lower.strip()
    word_right_lower=word_right_lower.strip()
    #Compare the words
    if word_to_check_lower != word_right_lower:
        compare_indicator=False
    return compare_indicator

def main():
    # Obtiene la lista con palabras correctas.
    list_rigth_words=file_to_list("wordlist.txt")
    # Get the new text and put it into a list
    text_to_spell=input("Write text: ")
    # text_to_spell="This is acually a good and usefull program"
    new_text_list=text_to_spell.split()
    text_spell_result=""
    #assume the words are differents
    for word_to_spell in new_text_list:
        word_to_spell_lower=word_to_spell.lower()
        # Set a flag for the check to false.
        word_found=False
        if word_to_spell_lower in list_rigth_words:
            word_found=True
        # for word_to_compare in list_rigth_words:
        #     if evaluate_words(word_to_spell,word_to_compare):
        #         word_found=True
        if word_found==False:
            word_to_spell="*"+word_to_spell+"*"
            text_spell_result=text_spell_result+word_to_spell+" "
        else:
            text_spell_result=text_spell_result+word_to_spell+" "
            continue
    text_spell_result=text_spell_result.strip()
    print(text_spell_result)
        


                





        

main()