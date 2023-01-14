# Laila Donaldson
# July 1, 2022
# Comp 163 Summer Session II
# This program will use quality points and credit hours of given courses to run
# a calculation which will determine and print the GPA for a semester.

quality_point_equivalency = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

# display the equivalency of the letter grades to the quality points for user reference
print ('Below are the grade quality point vales:\n', quality_point_equivalency, '\n')

# prompt the user to enter their course information
course1 = input('Enter your first class here: ')
course1_quality_points = float(input('Enter the number of quality points earned from this class: '))
course1_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course1_total_points = (course1_quality_points * course1_credit_hrs)
print()

course2 = input('Enter your second class here: ')
course2_quality_points = float(input('Enter the number of quality points earned from this class: '))
course2_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course2_total_points = (course2_quality_points * course2_credit_hrs)
print()

course3 = input('Enter your third class here: ')
course3_quality_points = float(input('Enter the number of quality points earned from this class: '))
course3_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course3_total_points = (course3_quality_points * course3_credit_hrs)
print()

course4 = input('Enter your fourth class here: ')
course4_quality_points = float(input('Enter the number of quality points earned from this class: '))
course4_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course4_total_points = (course4_quality_points * course4_credit_hrs)
print()

course5 = input('Enter your fifth class here: ')
course5_quality_points = float(input('Enter the number of quality points earned from this class: '))
course5_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course5_total_points = (course5_quality_points * course5_credit_hrs)
print()

course6 = input('Enter your sixth class here: ')
course6_quality_points = float(input('Enter the number of quality points earned from this class: '))
course6_credit_hrs = float(input('Enter the number of credit hours for this class: '))
course6_total_points = (course6_quality_points * course6_credit_hrs)
print()

# calculate the sum of credit hours and of total points from each course for final GPA calculation
total_credit_hrs = (course1_credit_hrs + course2_credit_hrs + course3_credit_hrs + course4_credit_hrs + course5_credit_hrs + course6_credit_hrs)
total_points = (course1_total_points + course2_total_points + course3_total_points + course4_total_points + course5_total_points + course6_total_points)
gpa = total_points/total_credit_hrs

print('Your GPA for the semester is:', f'{gpa:.2f}')
