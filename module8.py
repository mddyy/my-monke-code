# задача 8.1
print('Задача 8.1')
init_array = [10, 9, 10, 10, 9, 8, 7]
# старое решение
# result_array = [x for x in init_array
#                 if x in init_array[init_array.index(x) + 1:]]
counter_dict = {}
result_array = []
for x in init_array:
    counter_dict[x] = counter_dict.setdefault(x, 0) + 1
for x in init_array:
    if counter_dict[x] > 1:
        result_array.append(x)
print(f'{init_array} -> {result_array}')

# задача 8.2
print('\n\nЗадача 8.2')
# нейминги взяты из текста задачи
x = 1
y = 1
z = 1
n = 2
result = [
    [x_copy, y_copy, z_copy]
    for x_copy in [0, x]
    for y_copy in [0, y]
    for z_copy in [0, z]
    if x_copy + y_copy + z_copy != n
]
print(result)

# задача 8.3
print('\n\nЗадача 8.3')
# нейминги взяты из текста задачи
n = 7
result = [x * 2 for x in range(1, n, 2)]
print(result)

# задача 8.4
print('\n\nЗадача 8.4')

# задача 8.5
print('\n\nЗадача 8.5')

#рекурсивная функция вычисления чисел Фибоначчи
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


#первые 20 чисел Фибоначчи
fibonacci_generator = (fibonacci(x) for x in range(0, 20))


def transparency_calc(years):
    transparency = 10000
    for year in range(0, years):
        if year in fibonacci_generator:
            transparency -= year
        else:
            transparency += 1
        yield transparency


def age_calc(transparency):
    max_age = 5000
    age = 0
    for i in transparency_calc(max_age):
        if i == transparency:
            return age
        else:
            age += 1
    return -1


init_transparancy = 9999
print(f'возраст призрака с прозрачностью {init_transparancy} = {age_calc(init_transparancy)} лет')
