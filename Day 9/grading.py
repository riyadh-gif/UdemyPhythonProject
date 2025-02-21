student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, skor in student_scores.items():
    if 90 <= skor <= 100:
        student_grades[student] = "outstanding"
    elif 81 <= skor <= 91:
        student_grades[student] = "Exceeds Expectations"  
    elif 71 <= skor <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "fail"

print(student_grades)