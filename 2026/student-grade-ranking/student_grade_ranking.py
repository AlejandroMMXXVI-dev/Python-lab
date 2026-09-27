students = []
highest_grade = -1.0
highest_grade_name = ""
second_highest_grade = -1.0
second_highest_grade_name = ""
grade_sum = 0.0
number_of_students = 2

for i in range(number_of_students):
    print(f"Student Registration {i + 1}/{number_of_students}")

    name = input("Enter the student's name: ")
    grade = float(input(f"Enter {name}'s grade: "))

    students.append([name, grade])
    grade_sum += grade

    if grade > highest_grade:
        second_highest_grade = highest_grade
        second_highest_grade_name = highest_grade_name
        highest_grade = grade
        highest_grade_name = name

    elif grade > second_highest_grade and grade < highest_grade:
        second_highest_grade = grade
        second_highest_grade_name = name

class_average = grade_sum / number_of_students

students_above_average = 0

for student_name, student_grade in students:
    if student_grade > class_average:
        students_above_average += 1

print("\nFinal Results")
print(f"1st Place: {highest_grade_name} - {highest_grade:.1f}")
print(f"2nd Place: {second_highest_grade_name} - {second_highest_grade:.1f}")
print(f"Class Average: {class_average:.1f}")
