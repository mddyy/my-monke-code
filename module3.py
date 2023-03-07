# задача 3.1
print('Задача 3.1')
firstname = 'Vadim'
lastname = 'Kriulin'
print(f'Hello, {firstname} {lastname}! You just delved into Python. Great start!')

# задача 3.2
# немного криво с четными thickness
print('\n\nЗадача 3.2')
marker = '1'
thickness = 5
for i in range(thickness+1):
    print(f'{marker*(i*2-1): ^{thickness * 2}}')
for i in range(thickness):
    print(f'{marker*thickness: ^{thickness * 2}}' + ' '*thickness + f'{marker*thickness: ^{thickness * 2}}')
for i in range(thickness//2 + 1):
    print(f'{marker*thickness*4: ^{thickness * 5}}')
for i in range(thickness):
    print(f'{marker * thickness: ^{thickness * 2}}' + ' ' * thickness + f'{marker * thickness: ^{thickness * 2}}')
for i in range(thickness+1):
    print(' '*thickness * 3 + f'{marker*((thickness-i)*2-1): ^{thickness * 2}}')

# задача 3.3
print('\n\nЗадача 3.3')
text = """
cow goes moo
cat goes meow
junior goes hello world
"""
print(text.title())

# задача 3.4
print('\n\nЗадача 3.4')
amount = 12345.6788888
print(f'{amount:,.2f}')

# задача 3.5
print('\n\nЗадача 3.5')
height = 13
width = height * 3
for i in range(1, height//2 + 1):
    print('-' * ((width - (i * 3 * 2))//2 + 2) + '.|.' * (i * 2 - 1) + '-' * ((width - (i * 3 * 2))//2 + 2))
print(f'{"WECLOME":-^{width}}')
for i in range(height//2, 0, -1):
    print('-' * ((width - (i * 3 * 2))//2 + 2) + '.|.' * (i * 2 - 1) + '-' * ((width - (i * 3 * 2))//2 + 2))

# задача 3.6
print('\n\nЗадача 3.6')
value = 134099705
answer = 1
for i in str(value):
    if value % 10 != 0:
        answer *= value % 10
        value //= 10
    else:
        value //= 10
        continue
print(answer)
