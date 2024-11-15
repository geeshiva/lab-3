# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Joshua Downey"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101310030"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-60"

#==========================================#
# Place your student_health_list function after this line
import csv

def students_by_health(file_name, health_value):
    students = []
    with open("student-mat.csv", "r") as file:
        content = file.readlines()
    for i in content:
        info = i.split()
        if info.pop(4) == health_value:
            stu_dict = dict()
            stu_dict['school'] = info[0]
            stu_dict['age'] = info[1]                
            stu_dict['Studytime'] = info[2]
            stu_dict['Failures'] = info[3]
            stu_dict['Absences'] = info[4]
            stu_dict['G1'] = info[5]
            stu_dict['G2'] = info[6]
            stu_dict['G3'] = info[7]
            students.append(stu_dict)
            return print(students)
        
        
        

# Do NOT include a main script in your submission
