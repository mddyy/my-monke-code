# 1. Друзья.
#
# Создайте класс "Friends", который должен содержать данные о людях (их имена) и о связях между ними.
# Имена представлены в виде текстовых строк, чувствительных к регистру.
# Связи не имеют направлений, то есть, если существует связь "sofia" с "nikola", это справедливо и в обратную сторону.
#
# class Friends(connections)
#
# Возвращает новый объект, экземпляр класса Friends.
# Параметр "connections" имеет тип "итерируемый объект", содержащий множества (set) с двумя элементами в каждом.
# Каждая связь содержит два имени в виде текстовых строк.
# Связи могут повторяться в параметре инициализации, но в объекте хранятся только уникальные пары.
# Каждая связь имеет только два состояния - присутствует или не присутствует.
#
# add(connection)
#
# Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк).
# Возвращает True, если заданная связь новая и не присутствует в объекте.
# Возвращает False, если заданная связь уже существует в объекте.
#
# remove(connection)
#
# Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк).
# Возвращает True, если заданная связь существует в объекте.
# Возвращает False, если заданная связь не присутствует в объекте.
#
# names()
#
# Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.
#
# connected(name)
#
# Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name".
# Если "name" не присутствует в объекте, возвращается пустое множество (set).

class Friends:

    name_connections = {}
    friend_connections = []

    def __init__(self, connections):
        for connection in connections:
            self.add(connection)

    def __str__(self):
        return str(self.friend_connections)

    def __repr__(self):
        return f'Friends({self.friend_connections})'

    def add(self, connection: set) -> bool:
        if connection in self.friend_connections:
            return False

        self.friend_connections.append(connection.copy())
        one_friend = connection.pop()
        other_friend = connection.pop()
        self.name_connections.setdefault(one_friend, set()).add(other_friend)
        self.name_connections.setdefault(other_friend, set()).add(one_friend)
        return True

    def remove(self, connection: set) -> bool:
        if connection not in self.friend_connections:
            return False

        self.friend_connections.remove(connection)
        one_friend = connection.pop()
        other_friend = connection.pop()
        self.name_connections[one_friend].discard(other_friend)
        self.name_connections[other_friend].discard(one_friend)
        return True

    def names(self):
        return set(self.name_connections.keys())

    def connected(self, name: str) -> set:
        return self.name_connections.setdefault(name, set())


some_dudes = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
print(str(some_dudes))
some_dudes.remove({'c', 'b'})
print(str(some_dudes))
print(some_dudes.friend_connections)
print(some_dudes.names())
print(some_dudes.connected('b'))


# 2 Деканат
#
# спроектируйте следующую предметную область, используя объектно-ориентированный подход.
#
# Сотрудники деканата каждый семестр решают проблему формирования отчетных ведомостей студентов, разных групп и курсов.
# Цель - получить информацию о среднем балле каждого студента, группы, а также предмета
# (например, средний балл по физкультуре в группе 433 составляет 4.1).
# Такая информация поможет сформировать список студентов, которых нужно отчислить и стипендиатов,
# а также наиболее "проблемные" предметы.

class Student:
    def __init__(self, fio: str, course: int, group: str, **grades: int):
        self.fio = fio
        self.course = course
        self.group = group
        self.grades = grades
        self.avg_grade = self.avg_grade()

    def avg_grade(self):
        from statistics import mean
        return mean(self.grades.values())

    def __str__(self):
        return(f'{self.fio}, group {self.group}')


class Dekanat:

    students = []

    def __init__(self, students):
        self.students = set(students)

    def group_avg_grade(self, group: str) -> float:
        from statistics import mean
        group_list = []
        for student in self.students:
            if student.group == group:
                group_list += list(student.grades.values())
        return mean(group_list)

    def subject_avg_grade(self, subject: str) -> float:
        from statistics import mean
        subject_list = []
        for student in self.students:
            subject_list.append(student.grades[subject])
        return mean(subject_list)

    def avg_grades(self):
        """
        находит средний балл каждой группы по каждому предмету
        :param students: входной список студентов
        :return: словарь вида "группа: словарь средних оценок по предметам"
        """
        from collections import Counter
        grade_count = {}
        grade_average = {}

        for student in self.students:
            grade_count[student.group] = grade_count.setdefault(student.group, 0) + 1
            if student.group not in grade_average.keys():
                grade_average[student.group] = Counter()
                continue
            grade_average[student.group].update(student.grades)

        for group, grade_set in grade_average.items():
            for key in grade_set.keys():
                grade_set[key] /= grade_count[group]
            grade_average[group] = dict(grade_set)

        return grade_average

    def fellows(self):
        return [str(student) for student in self.students
                if set(student.grades.values()).intersection({0, 1, 2, 3}) == set()]

    def for_dropout(self):
        return [str(student) for student in self.students
                if set(student.grades.values()).intersection({0, 1, 2}) != set()]


studs = [
    Student('Vasya', 3, '333', matan=2, phys=3, pe=4, gpo=5, python=2),
    Student('Petya', 2, '222', matan=4, phys=5, pe=4, gpo=3, python=2),
    Student('Lesha', 2, '222', matan=4, phys=5, pe=4, gpo=5, python=5),
    Student('Masha', 3, '333', matan=5, phys=4, pe=5, gpo=3, python=2),
]

dekanat = Dekanat(studs)
print(f'average grade for group 333 is {1}', dekanat.group_avg_grade('333'))
print(dekanat.avg_grades())
print(f'average grade for matan is {1}', dekanat.subject_avg_grade('matan'))
print(dekanat.fellows())