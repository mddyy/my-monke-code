"""
задача 8.1 - Список из числа
Дано: натуральное число N.
Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
Пример:
123, результат: [3, 2, 1]
"""

print('Задача 9.1')


def reverse_digit(number: int):
    """
    :param number: натуральное число
    :return: список цифр числа в обратном порядке
    """
    reversed_digits = [int(digit) for digit in str(number)]
    reversed_digits.reverse()
    return reversed_digits


print(reverse_digit(12223))


"""
задача 9.2 - Палиндром
слово, состоящее только из строчных латинских букв.
Задание: написать функцию, которая возвращает True, если слово палиндромом, иначе False.
Примеры:
'lol', результат: True
'hi', результат: False
"""
print('\n\nЗадача 9.2')


def ispalindrome(word):
    """
    :param word: слово(строка)
    :return: true, если строка является палиндромом; false, если строка не является палиндромом
    """
    reversed_word = word[::-1]
    return reversed_word.lower() == word.lower()

print(ispalindrome('abcd'))
print(ispalindrome('Atmta'))


"""
задача 9.3 - Деканат
Дано: список студентов: каждый элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы, оценки по пяти предметам.
Задание: реализуйте сл. функции:
1) возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке;
2) находит средний балл каждой группы по каждому предмету;
3) определяет самого старшего студента и самого младшего студентов.
4) возвращает словарь, где для каждой группы определен лучшый с точки зрения успеваемости студент.
"""


class Student:
    def __init__(self, fio: str, birth_year: int, course: int, group: str, **grades: int):
        self._fio = fio
        self._birth_year = birth_year
        self._course = course
        self._group = group
        self._grades = grades
        self.__avg_grade = self.avg_grade()

    def __repr__(self):
        return (f'Student(fio={self._fio}, '
                f'birth_year={self._birth_year}, '
                f'course={self._course}, '
                f'group={self._group}) '
                f'# avg_grade={self.avg_grade()}')

    def __str__(self):
        return self._fio

    def avg_grade(self):
        from statistics import mean
        return mean(self._grades.values())

    @staticmethod
    def of_course(searching_course: int, students: list):
        """
        возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке
        :param searching_course: курс, который необходимо вывести
        :param students: входной список студентов
        :return: список студентов данного курса
        """
        course_list = [stud for stud in students if stud._course == searching_course]
        course_list.sort(key=lambda x: x._fio)
        return course_list

    @staticmethod
    def average_grades(students: list):
        """
        находит средний балл каждой группы по каждому предмету
        :param students: входной список студентов
        :return: словарь вида "группа: словарь средних оценок по предметам"
        """
        from collections import Counter
        grade_count = {}
        grade_average = {}

        for stud in students:
            grade_count[stud._group] = grade_count.setdefault(stud._group, 0) + 1
            if stud._group not in grade_average.keys():
                grade_average[stud._group] = Counter()
                continue
            grade_average[stud._group].update(stud._grades)

        for group, grade_set in grade_average.items():
            for key in grade_set.keys():
                grade_set[key] /= grade_count[group]
            grade_average[group] = dict(grade_set)

        return grade_average


def find_yongest_and_oldest(students: list):
    """
    находит самого младшего и самого старшего студентов из списка
    :param students: входной список студентов
    :return: кортеж из младшего и старшего студентов списка
    """
    youngest = max(students, key=lambda x: x._birth_year)
    oldest = min(students, key=lambda x: x._birth_year)
    return (youngest, oldest)


def find_best_student(students: list):
    """
    находит лучших с точки зрения успеваемости студентов каждой группы
    :param students:входной список студентов
    :return: словарь вида {группа: лучший_студент}
    """
    groups_best_grades = {}
    for stud in students:
        avg_grade = stud.avg_grade()
        if stud._group not in groups_best_grades.keys():
            groups_best_grades[stud._group] = (stud, avg_grade)
            continue
        if groups_best_grades[stud._group][1] < avg_grade:
            groups_best_grades[stud._group] = (stud, avg_grade)

    return groups_best_grades

print('\n\nЗадача 9.3')

studs = [
    Student('Vasya', 1999, 3, '333', matan=2, phys=3, pe=4, gpo=5, python=2),
    Student('Petya', 1998, 2, '222', matan=4, phys=5, pe=4, gpo=3, python=2),
    Student('Lesha', 1997, 2, '222', matan=4, phys=2, pe=4, gpo=5, python=2),
    Student('Masha', 1996, 3, '333', matan=5, phys=4, pe=5, gpo=3, python=2),
]

print('\nвозвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке')
print([str(stud) for stud in Student.of_course(3, studs)])

print('\nнаходит средний балл каждой группы по каждому предмету')
print(Student.average_grades(studs))

print('\nнаходит самого младшего и самого старшего студентов из списка')
print([stud for stud in find_yongest_and_oldest(studs)])

print('\nнаходит лучших с точки зрения успеваемости студентов каждой группы')
print(find_best_student(studs))

print('\nдля отладки: список всех студентов: ')
print([stud for stud in studs])


"""
задача 9.4 - Пешки
Вам предоставляется набор координат, в которых расставлены белые пешки. 
Вы должны подсчитать количество защищенных пешек.
"""

def count_protected_pawns(setup: set):
    """
    функция подсчета защищенных пешек на доске
    :param setup: setup - множество позиций на доске, на которых находятся пешки
    :return: количество защищенных пешек
    """
    cell_chars_list = {chr(c) for c in range(ord('a'), ord('i'))}
    cell_nums_list = {str(x) for x in range(1, 9)}

    #проверка корректности позиции. нужна для проверки входных данных и генерации позиций защитных пешек
    def is_position_correct(pos: str) -> bool:
        return (pos[0] in cell_chars_list
                and pos[1] in cell_nums_list
                and len(pos) == 2)

    #генерация позиций защитных пешек для данной позиции
    #метод может выйти за пределы доски, но потом исключит такие позиции
    def find_protector_cells(pos: str):
        new_cell_num = str(int(pos[1]) - 1)
        pos_char_ord = ord(pos[0])

        new_pos_1 = chr(pos_char_ord + 1) + new_cell_num
        new_pos_2 = chr(pos_char_ord - 1) + new_cell_num

        protectors = set()
        if is_position_correct(new_pos_1):
            protectors.add(new_pos_1)
        if is_position_correct(new_pos_2):
            protectors.add(new_pos_2)

        return protectors

    #проверка входных данных
    incorrect_positions = set()
    for position in setup:
        if not is_position_correct(position):
            incorrect_positions.add(position)
    if incorrect_positions != set():
        raise ValueError("Обнаружены неправильные позиции: ", incorrect_positions)

    #подсчет защищенных пешек. для каждой позиции генерируются защитные позиции.
    #если в любой из этих позиций есть пешка из набора входных данных, то позиция защищена
    protected_pawns_count = 0
    for position in setup:
        protector_cells = find_protector_cells(position)
        if setup.intersection(protector_cells) != set():
            protected_pawns_count += 1

    return protected_pawns_count


print('\n\nЗадача 9.4')
test_setup_1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
print(test_setup_1, ', результат: ', count_protected_pawns(test_setup_1))
test_setup_2 = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
print(test_setup_2, ', результат: ', count_protected_pawns(test_setup_2))




