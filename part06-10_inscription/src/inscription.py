# Write your solution here
def main():
    student_name=input("Whom should I sign this to:")
    file_name=input("Where shall I save it:")
    # student_name="Ada"
    # file_name="inscribed.txt"
    with open(file_name, "w") as my_file:
        my_file.write(f'Hi {student_name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team\n')

main()