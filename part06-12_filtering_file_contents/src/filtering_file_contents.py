# Write your solution here
#**********
#* Metodo 1
#**********
# with open("coders.csv", "w") as my_file:
#     my_file.write("Eric;Windows;Pascal;10\n")
#     my_file.write("Matt;Linux;PHP;2\n")
#     my_file.write("Alan;Linux;Java;17\n")
#     my_file.write("Emily;Mac;Cobol;9\n")

#**********
#* Metodo 2
#**********
# coders = []
# coders.append(["Eric", "Windows", "Pascal", 10])
# coders.append(["Matt", "Linux", "PHP", 2])
# coders.append(["Alan", "Linux", "Java", 17])
# coders.append(["Emily", "Mac", "Cobol", 9])

# with open("coders.csv", "w") as my_file:
#     for coder in coders:
#         line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
#         my_file.write(line+"\n")

#**********
#* Metodo 3
#**********
# with open("coders.csv", "w") as my_file:
#     for coder in coders:
#         line = ""
#         for value in coder:
#             line += f"{value};"
#         line = line[:-1]
#         my_file.write(line+"\n")
#*******************************************************
# Filtering the contents of a file
# Please write a function named filter_solutions() which
# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
#*******************************************************


#*********************FUNCTION**************************
#*********       escribir en un archivo         ********
#*******************************************************
def write_entry(current_file:str,entry:str)->bool:
    with open(current_file, "a") as my_file:
        my_file.write(f'{entry}\n')

#*********************FUNCTION**************************
#*********         test line           ********
# Toma una linea con el formato: Kirka;79-15;22 
# revisa que la operacion sea correcta y devuelve 
# Verdadero o Falso
#*******************************************************
def operation_test(line_to_test:str)->bool:
    test_flag=False
    line_to_test=line_to_test.stripe()
    parts = line_to_test.split(';')
    result=parts[2]
    operation=parts[1]
    print(operation)
    if '+' in operation:
        
    return test_flag



    def main():
        # open('incorrect.csv', 'w').close()
        # open('correct.csv', 'w').close()
        operation_test("Kirka;79-15;22")


    main()