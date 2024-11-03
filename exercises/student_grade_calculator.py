grades = {"Alice": [85, 90, 78], "Bob": [80, 85, 88], "Charlie": [90, 92, 85]}

def average_grade(grades):
    for student, scores in grades.items():
        avg = sum(scores) / len(scores)
        print(f"{student}'s average grade is {avg:.2f}")

average_grade(grades)
