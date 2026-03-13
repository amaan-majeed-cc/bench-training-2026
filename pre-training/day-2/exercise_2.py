# exercise_2.py — Grade book system

# Store 5 students as a list of dicts: [{name, scores: [list of scores], subject}].
# Write functions: calculate_average(scores), get_grade(avg), class_topper(students).
# Print a formatted report: student name | avg score | grade. Bold the top scorer's row (add '***
# TOP ***' to their line).
# Bonus: sort the report by average score (descending) without modifying the original list.

students = [
    {"name": "Ahmed", "scores": [85, 90, 78], "subject": "Maths"},
    {"name": "Daniyal", "scores": [42, 58, 77], "subject": "Science"},
    {"name": "Faheem", "scores": [70, 75, 80], "subject": "English"},
    {"name": "Usama", "scores": [33, 58, 44], "subject": "Maths"},
    {"name": "Amaan", "scores": [95, 94, 98], "subject": "Science"},
]

def calculate_average(scores):
	return sum(scores) // len(scores)

def get_student_avg(student):
    return calculate_average(student['scores'])

def class_topper(students):
	topper = ''
	highest = 0
	for student in students:
		student_marks = calculate_average(student['scores'])
		if student_marks > highest:
			highest = student_marks
			topper = student['name']
	return topper

def get_grade(avg):
    if avg >= 90: return "A*"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    return "F"

def generate_table(students):
		topper = class_topper(students)
		sorted_students = sorted(students, key=get_student_avg, reverse=True)
		for student in sorted_students:
			student_avg = calculate_average(student['scores'])
			grade = get_grade(student_avg)
			student_name = student['name']
			row = f"\t{student_name:10} |\t {student_avg} \t|\t {grade}\t"

			if student_name == topper:
				print(f"** {row} **")
			else:
				print(f"{row}")

generate_table(students)
