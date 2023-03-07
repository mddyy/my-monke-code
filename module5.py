# Задача 5.1
print('Задача 5.1')
number = 3
answer = ''
if number % 3 == 0:
    answer += 'Fizz '
if number % 5 == 0:
    answer += 'Buzz'
if answer == '':
    print(number)
else:
    print(answer)


# Задача 5.2
print('\n\nЗадача 5.2')
number = 22
if number % 2 == 1:
    print('Плохо')
elif number <= 5:
    print('Неплохо')
elif number <= 20:
    print('Так себе')
elif number > 20:
    print('Отлично')

# Задача 5.3
print('\n\nЗадача 5.3')
number = 8
for i in range(1, number + 1):
    print(i, end='')

# Задача 5.4
print('\n\nЗадача 5.4')
text = "How are you? Eh, ok. Low or Lower? Ohhh."
for c in text:
    if c.isupper():
        print(c, end='')

# Задача 5.5
print('\n\nЗадача 5.4')
string_in = 'Hello 2 world hello 1'
count = 0
answer = 'false'
for substr in string_in.split():
    if substr.isdigit():
        count = 0
    else:
        count += 1
    if count == 3:
        answer = 'true'
        break
print(answer)

# Задача 5.5
print('\n\nЗадача 5.5')
strings = ["bright aright", "ok"]
answer = ''
for substr in strings:
    answer += substr.replace('right', 'left') + ','
print(answer)
