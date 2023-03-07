import sys
from random import randint, random

# задача 4.1
print('\nзадача 4.1')
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
print(f'a = {a}, b = {b}, c = {c}, answer = {(a + b + c)/3}')

# задача 4.2
print('\nзадача 4.2')
x = randint(0, 100)
y = randint(0, 100)
print(f'x = {x}, y = {y}, x // y = {x // y}, x % y = {x % y}')

# задача 4.3
print('\nзадача 4.3')
r = random() * 100
print(f'r = {r} \n1) {r:.2f} \n2) {round(r)} \n3) {r:=012.2f}')

# задача 4.4
print('\nзадача 4.4')
x = 161512
print(f'x = {x} -> ', end='')
y = 0
for i in str(x):
    y *= 10
    y += x % 10
    x //= 10
print(y)
