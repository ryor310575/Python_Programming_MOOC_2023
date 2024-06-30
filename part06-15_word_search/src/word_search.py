# Write your solution here
#******************** FUNCTION *************************
#*********    look for asterisk wld card        ********
#*******************************************************
def asterisk_wild(search_term: str)->list:
    words_found=[]
    word_to_search=""
    if "*" in search_term: # Evalua que exista el termino *
        if search_term[0]=="*": # Verifica que este al inicio
            word_to_search=search_term[1:].lower() # Elimina el primer termino y lo lleva a miusculas
            with open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().endswith(word_to_search):# Revisa si la palabra finaliza con la cadena buscada
                        words_found.append(line.strip())
        elif search_term[-1]=="*":# Verifica que este al final
            word_to_search=search_term[:-1].lower()# Elimina el ultimo termino y lo lleva a miusculas
            with  open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().startswith(word_to_search): # Revisa si la palabra inicia con la cadena buscada
                        words_found.append(line.strip())
    else:
        words_found[0]="no asterisk"
    return words_found
#******************** FUNCTION *************************
#*********            change pos               ********
#*******************************************************
def change_pos(word:str,position:int,character:str)->str:
    new_word=""
    new_word=word[0:position]+character+word[(position+1):]
    return new_word

#******************** FUNCTION *************************
#*********       look for dot wild card          ********
#*******************************************************
def wild_card_words(search_list:list,wild_card:str)-> list:
    wild_words_list=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for word in search_list:
        dot_position=word.find(wild_card)
        if dot_position==-1: # Evalua que exista el termino DOT
            wild_words_list=search_list
            return wild_words_list
        else:
            i=0
            while i<len(alphabet):
                new_word=word[0:dot_position]+alphabet[i]+word[(dot_position+1):]
                wild_words_list.append(new_word)
                i+=1
    wild_words_list=wild_card_words(wild_words_list,wild_card)
    return wild_words_list

#******************** FUNCTION *************************
#*********       look for dot wild card         ********
#*******************************************************
def dot_wild(search_term:str)-> list:
    words_found=[]
    word_to_search=[]
    if "." in search_term: # Evalua que exista el termino DOT
        word_to_search=wild_card_words([search_term],".")
        with  open("words.txt") as my_file:
            for line in my_file:
                line=line.strip()
                if  line in word_to_search:
                    words_found.append(line)
    else:
        words_found[0]="no dot"
    return words_found
#********************   MAIN   *************************
#*********         Execute Find words           ********
#*******************************************************
def find_words(search_term: str)->list:
    words_found=[]
    if "*" in search_term:
        words_found=asterisk_wild(search_term)
    elif "." in search_term:
        words_found=dot_wild(search_term)
    else:
        with  open("words.txt") as my_file:
            for line in my_file:
                if line.strip() == search_term:
                    words_found.append(line.strip())
    return words_found

def main():
    #print(wild_card_words(["c.r.y"],"."))
    print(find_words("car.y"))
    print(find_words("c.r.y"))
    print(find_words("carr*"))
    print(find_words("*arry"))
    print(find_words("carry"))
main()