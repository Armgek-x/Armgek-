def calculate_group_average(students):
    if not students:
        return 0.0
    return sum(s.get_average_grade() for s in students) / len(students)

def count_excellent_students(students):
    return sum(1 for s in students if s.get_average_grade() >= 4.5)

def find_best_student(students):
    if not students:
        return None
    return max(students, key=lambda s: s.get_average_grade())