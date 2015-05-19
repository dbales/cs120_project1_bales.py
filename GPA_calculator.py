print
print('         XXX PYTHON   GPA   CALCULATORXXX      ')
print
print
#function that gets the input and spits out output

A = 4
B = 3
C = 2
D = 1
F = 0 

#input for 1st course.
print('Welcome! Let\s get started. ')
class1 = raw_input('Enter the title of the 1st course?:  ')
creditHr1 = int(raw_input('And how many credit hours was the course?:  '))
grade1 =raw_input('and what grade did you earn?: ')
print('Course: %6s Credit Hrs: %2d Grade: %S' ) % (class1, creditHr1, grade1 )

###input for 2nd course.
class2 = raw_input('Now for the second course:   ')
creditHr2 = int(raw_input('How many credit hours was this course?'))
grade2 =raw_input('And grade earned?')

###input for 3rd course.
class3 = raw_input('and the third course?:   ')
creditHr3 = int(raw_input('Number of credit hours?:  '))
grade3 =raw_input('Grade?:   ')
