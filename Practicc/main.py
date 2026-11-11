import random
from student import Student
from student_manager import StudentManager
from statistics import calculate_group_average, count_excellent_students, find_best_student
from file_manager import save_students, load_students

def main():
    manager = StudentManager()
    manager.students = load_students()

    while True:
        print("СИСТЕМА УПРАВЛЕНИЯ СТУДЕНТАМИ")
        print("1. Добавить студента")
        print("2. Показать всех студентов")
        print("3. Найти студента по ID")
        print("4. Удалить студента")
        print("5. Изменить данные студента")
        print("6. Добавить оценку студенту")
        print("7. Показать статистику")
        print("8. Показать студентов по группе")
        print("9. Случайный студент (выбор для ответа)")
        print("10. Сохранить данные")
        print("11. Загрузить данные")
        print("0. Выход")
        
        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                student_id = int(input("Введите ID (число): "))
                name = input("Введите ФИО студента: ")
                age = int(input("Введите возраст: "))
                if age < 16:
                    print("Ошибка: возраст студента должен быть не менее 16 лет.")
                    continue
                group = input("Введите группу: ")
                
                new_student = Student(student_id, name, age, group)
                manager.add_student(new_student)
            except ValueError:
                print("Ошибка ввода! ID и возраст должны быть числами.")

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            try:
                student_id = int(input("Введите ID для поиска: "))
                student = manager.find_student(student_id)
                if student:
                    print("-" * 30)
                    student.show_info()
                    print("-" * 30)
                else:
                    print("Студент не найден.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "4":
            try:
                student_id = int(input("Введите ID студента для удаления: "))
                manager.delete_student(student_id)
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "5":
            try:
                student_id = int(input("Введите ID студента для изменения: "))
                manager.update_student(student_id)
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "6":
            try:
                student_id = int(input("Введите ID студента: "))
                student = manager.find_student(student_id)
                if student:
                    grade = int(input("Введите оценку (от 2 до 5): "))
                    student.add_grade(grade)
                else:
                    print("Студент не найден.")
            except ValueError:
                print("Ошибка: оценка должна быть целым числом.")

        elif choice == "7":
            if not manager.students:
                print("Нет данных для статистики.")
            else:
                print("\nСтатистика")
                print(f"Всего студентов: {manager.count_students()}")
                print(f"Средний балл по всем: {calculate_group_average(manager.students):.2f}")
                print(f"Количество отличников: {count_excellent_students(manager.students)}")
                best = find_best_student(manager.students)
                if best:
                    print(f"Лучший студент: {best.name} (Средний балл: {best.get_average_grade():.2f})")
        elif choice == "8":
            group = input("Введите название группы: ")
            group_students = manager.find_by_group(group)
            if not group_students:
                print("В этой группе нет студентов.")
            else:
                print(f"\nСтуденты группы {group}:")
                for s in group_students:
                    print(s)

        elif choice == "9":
            if not manager.students:
                print("Список студентов пуст.")
            else:
                rand_student = random.choice(manager.students)
                print(f"\nСлучайный студент для ответа: {rand_student.name} (Группа: {rand_student.group})")

        elif choice == "10":
            save_students(manager.students)

        elif choice == "11":
            manager.students = load_students()
            print("Данные загружены.")

        elif choice == "0":
            save_students(manager.students)
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный пункт меню. Пожалуйста, выберите от 0 до 11.")

if __name__ == "__main__":
    main()