# задача 7.1
print('Задача 7.1')
text = "hello, word of word"
text.strip(',. ')

chars_popularity = {}
for char in text:
    chars_popularity[char] = chars_popularity.setdefault(char, 0) + 1
print('chars popularity', chars_popularity)

import re
words_popularity = {}
splitted_text = re.split(r'[., ]', text)
for word in text.split():
    words_popularity[word] = words_popularity.setdefault(word, 0) + 1
print('words popularity: ', words_popularity)

# задача 7.2
print('\n\nЗадача 7.2')
dec_number = 2987
dec_to_latin = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}
latin_number = ''
for key, value in dec_to_latin.items():
    repeats = dec_number // key
    latin_number += value * repeats
    dec_number -= key * repeats
print(latin_number)

# задача 7.3
print('\n\nЗадача 7.3')
rates = {'Sberbank': 55.8, 'VTB24': 53.91, 'NEKIDALOWOBANK': 10.1, '2007BANK': 25}
best_rate = min(rates.values())
best_bank = ''
for key, value in rates.items():
    if value == best_rate:
        best_bank = key
        break
print(best_bank)

# задача 7.4
print('\n\nЗадача 7.4')
book = {'Petr': '546810', 'Katya': '241815'}
inverted_book = dict(zip(book.values(), book.keys()))
print(inverted_book)

# задача 7.5
print('\n\nЗадача 7.5')
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
rate_dict = dict(zip(dates, rates))
print(rate_dict)

# задача 7.6
print('\n\nЗадача 7.6')
def is_same_symbol(line):
    return line == line[0] * len(line)

data = [
    "OOX",
    "XXO",
    "OXX"
]

winner = 'D'
data_as_string = data[0] + data[1] + data[2]
win_cases = [
    data[0],
    data[1],
    data[2],
    data_as_string[0::3],
    data_as_string[1::3],
    data_as_string[2::3],
    data_as_string[0::4],
    data_as_string[2::4]
]

for case in win_cases:
    if is_same_symbol(case) and case[0] != '.':
        winner = case[0]
        break

print(winner)
