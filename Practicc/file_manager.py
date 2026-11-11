import json
import os
from student import Student

def save_students(students, filename="data/students.json"):
    data = []
    for s in students:
        data.append({
            "student_id": s.student_id,
            "name": s.name,
            "age": s.age,
            "group": s.group,
            "grades": s.grades
        })
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в файл.")

def load_students(filename="data/students.json"):
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            students = []
            for item in data:
                s = Student(
                    student_id=item["student_id"],
                    name=item["name"],
                    age=item["age"],
                    group=item["group"],
                    grades=item["grades"]
                )
                students.append(s)
            return students
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []