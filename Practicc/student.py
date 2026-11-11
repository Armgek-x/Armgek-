class Student:
    def init(self, student_id, name, age, group, grades=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.group = group
        self.grades = grades if grades is not None else []

    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average_grade():.1f}")
        print(f"Статус: {self.get_status()}")

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
            print("Оценка добавлена.")
        else:
            print("Ошибка: оценка должна быть в диапазоне от 2 до 5!")

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        avg = self.get_average_grade()
        if not self.grades:
            return "Нет оценок"
        elif avg >= 4.5:
            return "Отличник"
        elif avg >= 3.0:
            return "Успевающий"
        else:
            return "Неуспевающий"

    def str(self):
        return f"ID: {self.student_id} | {self.name} | Группа: {self.group} | Ср. балл: {self.get_average_grade():.1f}"