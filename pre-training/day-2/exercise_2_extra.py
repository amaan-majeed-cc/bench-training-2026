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
	# Since Students is already sorted, won't really need this here
	return sum(scores) // len(scores)

def class_topper(students):
	# Since Students is already sorted, won't really need this here
	return students[0]

def get_student_avg(student):
		return sum(student['scores']) // len(student['scores'])

def save_avg_scored(students):
	for student in students:
		student['scores'] = get_student_avg(student)

def get_grade(avg):
    if avg >= 90: return "A*"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    return "F"

def generate_table(students):
	for index, student in enumerate(students):
		row = f"\t{student['name']:10} |\t {student['scores']} \t|\t {get_grade(student['scores'])}\t"

		if index == 0:
			print(f"** {row} **")
		else:
			print(f"{row}")

copy_students = [s.copy() for s in students]
sorted_students = sorted(copy_students, key=lambda x: get_student_avg(x), reverse=True)

save_avg_scored(sorted_students)

generate_table(sorted_students)


