# 1. Случайности не случайны.
# Дано: n - целое число.
# Задание: написать функцию-генератор, которая возвращает n дробных чисел из диапазона [0, n]. Используйте функцию random.uniform для генерации случайных чисел.

from random import uniform
def rand_generator(n: int):
    for x in range(n):
        yield uniform(0, n)

n = 5
print('\n11.1')
print(f'for n = {n}: ', list(rand_generator(n)))


# 2. Ленивое объединение
# Дано: 2 списка произвольной длины.
# Задание: написать функцию, которая возвращает результат объединения этих списков. Используйте функцию itertools.chain.

from itertools import chain
def unite_lists(list_a: list, list_b: list) -> list:
    return list(chain(list_a, list_b))


list_a = [1, 2, 3]
list_b = [4, 5]
print('\n11.2')
print(f'for a = {list_a}, b = {list_b}:  a + b = ', unite_lists(list_a, list_b))


# 3. Рефакторинг.
# Дано: неоптимальный код.
# Задание: оптимизировать следующий код.
#
# def responses_creator(item_ids):
#     item_ids = [None] if item_ids is None else item_ids
#
#     responses = []
#     for item_id in item_ids:
#         new_response = dict(item_id=item_id)
#         responses.append(new_response)
#     return responses

def responses_creator(item_ids: list) -> list[dict]:
    item_ids = [None] if item_ids is None else item_ids
    return [{'item_id': x} for x in item_ids]

item_ids = [1, 2, 3, 4]
print('\n11.3')
print(f'for item_ids = {item_ids}: result = ', responses_creator(item_ids))
print(f'for item_ids = {[]}: result = ', responses_creator([]))
print(f'for item_ids = {None}: result = ', responses_creator(None))
