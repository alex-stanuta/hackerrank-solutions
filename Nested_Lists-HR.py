# Given the names and grades for each student in a Physics class of n students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, n, the number of students.
# The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

if __name__ == '__main__':
    physics = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        physics.append([name,score])
    grades = []
    students = []
    for i in physics:
        grades.append(i[1])
    second_grade = 0
    grades.sort()
    lowest_grade = grades[0]
    for i in grades:
        if i > lowest_grade:
            second_grade = i
            break
    for i in physics:
        if i[1] == second_grade:
            students.append(i[0])
    students.sort()
    for i in students:
        print(i)
