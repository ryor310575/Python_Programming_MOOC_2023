# Write your solution here
#******************** FUNCTION *************************
#*********    look for asterisk wld card        ********
#*******************************************************
def asterisk_wild(search_term: str)->list:
    words_found=[]
    word_to_search=""
    if "*" in search_term:
        if search_term[0]=="*":
            word_to_search=search_term[1:].lower()
            with open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().endswith(word_to_search):
                        words_found.append(line.strip())
        elif search_term[-1]=="*":
            word_to_search=search_term[:-1].lower()
            with  open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().startswith(word_to_search):
                        words_found.append(line.strip())
    else:
        word_found[0]="no asterisk"
    return words_found

def find_words(search_term: str)->list:
    words_found=asterisk_wild(search_term)
    return words_found

def main():
    print(find_words("carry*"))
main()