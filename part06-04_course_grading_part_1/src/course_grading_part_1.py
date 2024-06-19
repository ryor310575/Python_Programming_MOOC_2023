# write your solution here
#******************************************
# #*********  Este programa abre el archivo multiples veces ********* 
# with open("people.csv") as new_file:
#     # print out the names
#     for line in new_file:
#         parts = line.split(";")
#         print("Name:", parts[0])

#     # find the oldest
# with open("people.csv") as new_file:
#     age_of_oldest = -1
#     for line in new_file:
#         parts = line.split(";")
#         name = parts[0]
#         age = int(parts[1])
#         if age > age_of_oldest:
#             age_of_oldest = age
#             oldest = name
#     print("the oldest is", oldest)
# #********* Este programa abre el archivo slo una vez *********
# people = []
# # read the contents of the file and store it in a list
# with open("people.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         people.append((parts[0], int(parts[1]), parts[2]))
#         print(type(people[0]))

# # print out the names
# for person in people:
#     print("Name:", person[0])

# # find the oldest
# age_of_oldest = -1
# for person in people:
#     name = person[0]
#     age = person[1]
#     if age > age_of_oldest:
#         age_of_oldest = age
#         oldest = name
# print("the oldest is", oldest)

#******************************************
#********* Creando un Diccionario *********
# This following program creates a dictionary grades based on the contents of the file. 
# The keys are the names of the students, and the value attached to each key is the list 
# of grades attained by the student. The program converts the grades to integer values, 
# so they can be processed easier.
# grades = {}
# with open("grades.csv") as new_file:
#     for line in new_file:
#         line = line.replace("\n", "")
#         parts = line.split(";")
#         name = parts[0]
#         grades[name] = []
#         for grade in parts[1:]:
#             grades[name].append(int(grade))
# print(grades)
# # Now we can print out some statistics on each student based on the contents of the dictionary grades:
# for name, grade_list in grades.items():
#     best = max(grade_list)
#     average = sum(grade_list) / len(grade_list)
#     print(f"{name}: best grade {best}, average {average:.2f}")
#******************************************************************************
#********* strip() Removing unnecessary lines, spaces and line breaks *********
#******************************************************************************
# last_names = []
# with open("people2.csv") as new_file:
#     for line in new_file:
#         parts = line.split(";")
#         # ignore the header line
#         if parts[0] == "first":
#             continue
#         last_names.append(parts[1])
# print(last_names)
# a more efficient solution is to use the Python string method strip, which removes whitespace from 
# the beginning and end of a string. It removes all spaces, line breaks, tabs and other characters 
# which would not normally be printed out.
# last_names = []
# with open("people2.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "first":
#             continue # this was the header line, so it is ignored
#         last_names.append(parts[1].strip())
# print(last_names)

#******************************************
#********* Combining data from different files *********
#******************************************
# # Create the Name dictionary
# names = {}
# with open("employees.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic": # Obvia la cabecera
#             continue
#         names[parts[0]] = parts[1:] # Crear el diccionario

# # Create the Salaries dictionary
# salaries = {}
# with open("salaries.csv") as new_file:
#     for line in new_file:
#         parts = line.split(';')
#         if parts[0] == "pic":  # Obvia la cabecera
#             continue
#         salaries[parts[0]] = int(parts[1]) +int(parts[2])  # Crear el diccionario
# # Create the Incomes
# print("incomes:")
# for pic, name in names.items():
#     if pic in salaries:
#         salary = salaries[pic]
#         print(f"{name[0]:20} {salary} euros")
#     else:
#         print(f"{name[0]:20} 0 euros")


#******************************************
#********* Combining data from different files *********
#******************************************
# Crear el diccionario de estudiantes
students_file=input("Student information: ")
student_info= {}
with open(students_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id": # Obvia la cabecera
            continue
        student_info[parts[0]] = parts[1:] # Crear el diccionario de estudiantes

# Create the Salaries dictionary
exercice_file=input("Exercises completed: ")
student_exercises = {}
with open(exercice_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":  # Obvia la cabecera
            continue
        exercises=[]
        for exercise in parts[1:]:
            exercises.append(int(exercise))
        student_exercises[parts[0]] = exercises  # Crear el diccionario
# Create the report
for pic, name in student_info.items():
    if pic in student_exercises:
        exercises_completed = sum(student_exercises[pic])
        print(f"{name[0]} {name[1].strip()} {exercises_completed}")
    else:
        continue