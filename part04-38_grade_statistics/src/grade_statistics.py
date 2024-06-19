# Write your solution here
# Collect data from the students
def collect_data() -> list:
    data_list=[]
    while True:
        student_data=input("Exam points and exercises completed: ")
        if student_data=="":
            break
        data_list.append(student_data)
    return data_list
# Toma una cadena con dos numeros y devuele un puntaje 
# de la conversion de 0 - 100 a 0 - 10
def convert_answered_questions(data_str:str,position:int)->int:
    list_10_2_100 = list(data_str.split(" "))
    number_10_2_100=int(list_10_2_100[position])
    number_10_2_100=number_10_2_100/10
    return number_10_2_100

# Grade Calculations this take a list of strings and return a 
# List of integers
def grade_calculations(data_list:list,passing=False)->list:
    grade_list=[]
    for data_pair in data_list:
        answered_questions=convert_answered_questions(data_pair,1)
        exam_points=int(list(data_pair.split(" "))[0])
        if exam_points < 10 and passing==True:
            grade_list.append(0)
        else:
            grade_list.append(int(exam_points+answered_questions))
    return grade_list
# normaliza la escala de 0 a 30 a una escala de 0 a 5
def grade_normalzation(data_number:int)->int:
    data_normal=0
    if data_number>=0  and data_number < 15:
        data_normal=0
    elif data_number>=15  and data_number < 18:
        data_normal=1
    elif data_number>=18  and data_number < 21:
        data_normal=2
    elif data_number>=21  and data_number < 24:
        data_normal=3
    elif data_number>=24  and data_number < 28:
        data_normal=4
    elif data_number>=28  and data_number <= 30:
        data_normal=5
    return data_normal

# Normaliza una lista de valores
def list_normalzation(data_list:list)->list:
    list_normal=[]
    for data in data_list:
        list_normal.append(grade_normalzation(data))
    return list_normal

# Points average function select the average from
def data_average(data_list:list)->float:
    avrg=0
    for data in data_list:
        avrg=avrg + float(data)
    avrg=avrg/len(data_list)
    return avrg

# Pass Percentage function
def data_passing(data_list:list)->float:
    passing=0
    new_list=list_normalzation(grade_calculations(data_list,True))
    for data in new_list:
        if data > 0:
            passing +=1
    passing = 100 * passing/len(new_list)
    return passing
# stars line
def star_line(times):
    i = 0
    line=""
    while i < times or len(line) < times:
        line = line + "*"
        i += 1
    return line

# Frequency in stars
def frequency_stars(data_list:list)->list:
    star_list=[]
    counter_i = 0
    counter_i = data_list.count(5)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(4)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(3)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(2)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(1)
    stars = star_line(counter_i)
    star_list.append(stars)
    counter_i = data_list.count(0)
    stars = star_line(counter_i)
    star_list.append(stars)
    return star_list

# the main function
def main():
    my_list=collect_data()
    processed_list=list_normalzation(grade_calculations(my_list,True))
    print("Statistics:")
    print(f'Points average: {data_average(grade_calculations(my_list)):.1f}')
    print(f'Pass percentage: {data_passing(my_list):.1f}')
    print("Grade distribution:")
    print(f'5: {frequency_stars(processed_list)[0]}')
    print(f'4: {frequency_stars(processed_list)[1]}')
    print(f'3: {frequency_stars(processed_list)[2]}')
    print(f'2: {frequency_stars(processed_list)[3]}')
    print(f'1: {frequency_stars(processed_list)[4]}')
    print(f'0: {frequency_stars(processed_list)[5]}')

# run the main function
main()