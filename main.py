def ave_rate_lector(self):
    summ = 0
    length = 0
    for key, value in self.grades_for_lector.items():
        summ += sum(value)
        length += len(value)
    return summ / length

def ave_rate_student(self):
    summ = 0
    length = 0
    for key, value in self.grades.items():
        summ += sum(value)
        length += len(value)
    return summ / length

def ave_rate_students_course(students, course):
    summ = 0
    length = 0
    for student in students:
        for key, value in student.grades.items():
            if key in course:
                summ += sum(value)
                length += len(value)
    return summ / length

def ave_rate_lecturers_course(lecturers, course):
    summ = 0
    length = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades_for_lector.items():
            if key in course:
                summ += sum(value)
                length += len(value)
    return summ / length

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lector:    
                lecturer.grades_for_lector[course] += [grade]
            else:
                lecturer.grades_for_lector[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {ave_rate_student(self)}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершённые курсы: {self.finished_courses}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return ave_rate_student(self) < ave_rate_student(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades_for_lector = {}
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {ave_rate_lector(self)}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturor')
            return
        return ave_rate_lector(self) < ave_rate_lector(other)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Mark', 'Watson', 'man')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

pretty_reviewer = Reviewer('Simma', 'Magg')
pretty_reviewer.courses_attached += ['Python']
pretty_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
pretty_reviewer.rate_hw(bad_student, 'Python', 7)
pretty_reviewer.rate_hw(bad_student, 'Git', 8)

best_lecturer = Lecturer('Sam', 'Smith')
best_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Ann', 'Showey')
bad_lecturer.courses_attached += ['Python']

best_student.rate_lection(best_lecturer, 'Python', 9)
bad_student.rate_lection(bad_lecturer, 'Python', 4)

print(cool_reviewer)
print(best_lecturer)
print(best_student)
print(best_lecturer < bad_lecturer)
print(best_student < bad_student)
print(ave_rate_students_course([bad_student, best_student], 'Python'))
print(ave_rate_lecturers_course([bad_lecturer, best_lecturer], 'Python'))