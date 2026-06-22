class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0
        else:
            avg_grade = 0

        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

    def get_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0
        return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0
        else:
            avg_grade = 0

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()

    def get_average_grade(self):
        if self.grades:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return sum(all_grades) / len(all_grades) if all_grades else 0
        return 0


class Reviewer(Mentor):
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_hw_grade_for_course(students_list, course_name):
    total_grades = []
    for student in students_list:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])

    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecture_grade_for_course(lecturers_list, course_name):
    total_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])

    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0


student1 = Student('Иван', 'Иванов', 'МУЖ')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Ульяна', 'Ульянова', 'ЖЕН')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Основы алгоритмов']
student3 = Student('Алексей', 'Алексеев', 'МУЖ')  # Студент без курсов
student3.courses_in_progress += []  # Не изучает никакие курсы


reviewer1 = Reviewer('Петр', 'Петров')
reviewer1.courses_attached += ['Python', 'Git']
reviewer2 = Reviewer('Евегния', 'Евгенева')
reviewer2.courses_attached += ['Python', 'Java']
reviewer3 = Reviewer('Сергей', 'Сергеев')  # Проверяющий без привязанных курсов
reviewer3.courses_attached += []  # Не привязан ни к одному курсу


lecturer1 = Lecturer('Дмитрий', 'Дмитриев')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Надежда', 'Надеждина')
lecturer2.courses_attached += ['Python', 'Java']


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 7)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 8)


lecturer1.grades['Python'] = [9, 10, 8, 9]
lecturer1.grades['Git'] = [7, 8]

lecturer2.grades['Python'] = [10, 10, 9, 10]
lecturer2.grades['Java'] = [8, 9, 8]


print("Информация о студентах:")
print(student1)
print()
print(student2)
print()

print("Информация о проверяющих:")
print(reviewer1)
print()
print(reviewer2)
print()

print("Информация о лекторах:")
print(lecturer1)
print()
print(lecturer2)
print()


print("Сравнение студентов:")
print(f"Средняя оценка {student1.name} {student1.surname}: {student1.get_average_grade():.1f}")
print(f"Средняя оценка {student2.name} {student2.surname}: {student2.get_average_grade():.1f}")
print(f"{student1.name} {student1.surname} > {student2.name} {student2.surname}: {student1 > student2}")
print(f"{student1.name} {student1.surname} < {student2.name} {student2.surname}: {student1 < student2}")
print(f"{student1.name} {student1.surname} == {student2.name} {student2.surname}: {student1 == student2}")
print()


print("Сравнение лекторов:")
print(f"Средняя оценка {lecturer1.name} {lecturer1.surname}: {lecturer1.get_average_grade():.1f}")
print(f"Средняя оценка {lecturer2.name} {lecturer2.surname}: {lecturer2.get_average_grade():.1f}")
print(f"{lecturer1.name} {lecturer1.surname} > {lecturer2.name} {lecturer2.surname}: {lecturer1 > lecturer2}")
print(f"{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} {lecturer1.surname} == {lecturer2.name} {lecturer2.surname}: {lecturer1 == lecturer2}")
print()


print("Подсчет средних оценок:")
students_list = [student1, student2]
course_name = 'Python'
avg_hw = average_hw_grade_for_course(students_list, course_name)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw:.1f}")

course_name = 'Git'
avg_hw = average_hw_grade_for_course(students_list, course_name)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw:.1f}")

course_name = 'Java'
avg_hw = average_hw_grade_for_course(students_list, course_name)
print(f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw:.1f}")
print()

lecturers_list = [lecturer1, lecturer2]
course_name = 'Python'
avg_lecture = average_lecture_grade_for_course(lecturers_list, course_name)
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture:.1f}")

course_name = 'Git'
avg_lecture = average_lecture_grade_for_course(lecturers_list, course_name)
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture:.1f}")

course_name = 'Java'
avg_lecture = average_lecture_grade_for_course(lecturers_list, course_name)
print(f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture:.1f}")
print()

print('-' * 25)

# Ситуация, когда Проверяющий пытается выставить оценку по курсу, который не привязан к проверяющему
print("Проверяющий Петров пытается выставить оценку по курсу Java (не привязан к Петрову)")
result3 = reviewer1.rate_hw(student2, 'Java', 8)
print(f"Результат: {result3}")
print("Ошибка: Проверяющий Петров не привязан к курсу Java")
print()

# Ситуация, когда Проверяющий пытается выставить оценку студенту по курсу, который студент не изучает
print("Проверяющий Петров пытается выставить оценку студенту Иванову по курсу Java (не изучает)")
result4 = reviewer1.rate_hw(student1, 'Java', 8)
print(f"Результат: {result4}")
print("Ошибка: Студент Иванов не изучает курс Java")
print()

# Ситуация, когда Проверяющий без привязанных курсов пытается выставить оценку
print("Проверяющий Сергеев (без привязанных курсов) пытается выставить оценку")
result5 = reviewer3.rate_hw(student1, 'Python', 8)
print(f"Результат: {result5}")
print("Ошибка: Проверяющий Сергеев не привязан ни к одному курсу")
print()

# Ситуация, когда Студент без курсов в процессе изучения
print("Проверяющий Петров пытается выставить оценку студенту Алексееву (без курсов)")
result6 = reviewer1.rate_hw(student3, 'Python', 8)
print(f"Результат: {result6}")
print("Ошибка: Студент Алексеев не изучает курс Python")
print()

# Ситуация, когда Передан не студент
print("Проверяющий Петров пытается выставить оценку объекту, который не является студентом")
result7 = reviewer1.rate_hw(reviewer1, 'Python', 8)
print(f"Результат: {result7}")
print("Ошибка: Переданный объект не является экземпляром класса Student")
print()

# Ситуация, когда Проверяющий пытается выставить оценку студенту по курсу, который есть у студента, но нет у проверяющего
print("Проверяющий Евгения (привязана к Python и Java) пытается выставить оценку по курсу Git")
result8 = reviewer2.rate_hw(student1, 'Git', 8)
print(f"Результат: {result8}")
print("Ошибка: Проверяющий Евгения не привязана к курсу Git, хотя студент Иванов его изучает")