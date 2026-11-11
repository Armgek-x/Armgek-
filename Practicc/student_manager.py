from student import Student

class StudentManager:
    def init(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.student_id == student.student_id:
                print("Ошибка: Студент с таким ID уже существует!")
                return False
        self.students.append(student)
        print("Студент успешно добавлен!")
        return True

    def show_students(self):
        if not self.students:
            print("Список студентов пуст.")
            return
        print("\nСписок студентов")
        for student in self.students:
            print(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print("Студент удален.")
        else:
            print("Ошибка: Студент с таким ID не найден.")

    def update_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            print("Студент не найден.")
            return

        print(f"Редактирование студента: {student.name}")
        new_name = input("Введите новое ФИО (оставьте пустым для пропуска): ")
        if new_name:
            student.name = new_name

        new_age = input("Введите новый возраст (оставьте пустым для пропуска): ")
        if new_age:
            try:
                student.age = int(new_age)
            except ValueError:
                print("Ошибка: возраст должен быть числом.")

        new_group = input("Введите новую группу (оставьте пустым для пропуска): ")
        if new_group:
            student.group = new_group

        print("Данные успешно обновлены!")

    def find_by_group(self, group_name):
        return [s for s in self.students if s.group.lower() == group_name.lower()]

    def count_students(self):
        return len(self.students)