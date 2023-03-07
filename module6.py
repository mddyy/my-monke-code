# Задача 6.1
import statistics

print('Задача 6.1')
elements = [1, 1, 1, 4, 4]
result = 0
if len(elements) > 0:
    result = sum(elements[0::2]) * elements[-1]
print(result)

# Задача 6.2
print('\n\nЗадача 6.2')
elements = [1, 1, 1, 4, 10.1111]
result = 0
if len(elements) > 0:
    result = max(elements) - min(elements)
print(f'{result:.4g}')

# Задача 6.3
print('\n\nЗадача 6.3')
elements = (-20, -5, 10)
result = []
if len(elements) > 0:
    # почему среда разработки ругается на эту строчку?
    result = sorted(elements, key=abs)
print(result)

# Задача 6.4
print('\n\nЗадача 6.4')
elements = [1, 2, 3, 4, 5, 5]
result = statistics.median(elements)
print(result)

# Задача 6.5
print('\n\nЗадача 6.5')
import re
# гласные и согласные, как списки
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
text = "Dog,cat,mouse,bird.Human."
# разбиение исходного текста на слова по набору разделителей
# при этом весь текст переводится в верхний регистр для удобатва сравнения
splittedText = re.split(r'[., ]', text.upper())
answer = 0
# цикл проходит все слова в тексте
for s in splittedText:
    # отбросить пустые строки и слова из одной буквы
    if len(s) <= 1:
        continue
    # разбиение слов на четные и нечетные по порядку буквы
    # слово считается "полосатым", если все четные буквы - гласные, а все нечетные - согласные,
    # либо наоборот
    substr1 = list(s[0::2])
    substr2 = list(s[1::2])
    # проверка, принадлежат ли все элементы множества substrN множеству гласных/согласных
    flag1 = all(x in consonants for x in substr1)
    flag2 = all(x in vowels for x in substr2)
    flag3 = all(x in vowels for x in substr1)
    flag4 = all(x in consonants for x in substr2)
    if flag1 and flag2 or flag3 and flag4:
        answer += 1
print(answer)
