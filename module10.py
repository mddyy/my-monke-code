# 1. Градусник
# Дано: список градусов Цельсия.
# Задание: написать функцию, которая преобразовывает исходный список градусов Цельсия в список градусов Фаренгейта



def fc_converter(temp: list[float]) -> list[float]:
    return [x * 9 / 5 + 32 for x in temp]


data_in = [39.2, 36.5, 37.3, 37.8, 100]
print('\n10.1')
print(f'Температуры в гр. Цельсия: {data_in}')
print(f'В гр. Фаренгейта {fc_converter(data_in)}')


# 2. Длинномер
# Дано: список строковых значений.
# Задание: написать функцию, которая возвращает список длин каждой строки.

def length_counter(str_list: list[str]) -> list[int]:
    # старое решение
    # return [len(s) for s in str_list]
    return list(map(len, str_list))


data_in = ['Tina', 'Raj', 'Tom']
print('\n10.2')
print(f'Исходные строки: ', data_in)
print(f'Их длины: ', length_counter(data_in))


# 3. Рефакторинг.
# Дано: неоптимальный код.
# Задание: оптимизировать следующий код.
#
# sentences = ['капитан джек воробей',
#              'капитан дальнего плавания',
#              'ваша лодка готова, капитан']
#
# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')
#
# print(cap_count)

from functools import reduce
sentences = ['капитан джек воробей',
              'капитан дальнего плавания',
              'ваша лодка готова, капитан',
             'капитан, капитан, улыбнитесь']

cap_count = reduce(lambda x, y: x + y.count('капитан'), sentences, 0)
print('\n10.3')
print(cap_count)


# 4. Возведение в степень.
# Дано: два списка одинаковой длины: чисел X и степеней Y.
# Задание: написать функцию, которая возвращает список [x1^y1, x2^y2, ..], где X=[x1, x2, ..], Y=[y1, y2, ..].

def pow_lists(x, y: list) -> list:
    result = map(pow, x, y)
    return list(result)


X = [2, 3, 4]
Y = [10, 11, 12]
print('\n10.4')
print(pow_lists(X, Y))


# 5. Ленивая функция.
# Дано: цело число n.
# Задание: написать функцию-генератор, которая будет "лениво" возвращать значения от 0 до n, определенные следующими правилами.
# Если
# x == 0 -> -10
# x % 3 -> 45
# x % 5 -> (x / 5) + 93
#
# Иначе
# -> x / 2

def lazy_function(n):
    for x in range(n):
        if x == 0:
            yield -10
        elif x % 3:
            yield 45
        elif x % 5:
            yield (x / 5) + 93
        else:
            yield x/2


print('\n10.5')
n = 9
print(f'n = {n}: ', list(lazy_function(n)))


# 6. Самый большой прямоугольник.
# Дано: список высот всех столбцов в гистограмме (список целых чисел).
# Задание: У вас есть гистограмма. Попробуйте найти размер самого большого прямоугольника, который можно построить из столбцов гистограммы.

def largest_histogram(histogram: list[int]) -> int:
    def rectangle_length(start_pos: int, height: int) -> int:
        width = 0
        for x in histogram[start_pos::]:
            if x >= height:
                width += 1
                continue
            else:
                break
        return width

    max_rectangle = max(histogram)
    histogram_length = len(histogram)
    for i in range(histogram_length):
        for j in range(histogram[i])[-1::-1]:
            temp_rectangle = rectangle_length(i, j + 1) * (j + 1)
            if temp_rectangle > max_rectangle:
                max_rectangle = temp_rectangle
    return max_rectangle


print('\n10.5')
data_in = [1, 1, 3, 1]
print(f'largest in {data_in} == ', largest_histogram(data_in))
