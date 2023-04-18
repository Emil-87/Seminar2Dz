# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


def task1():
    number = int(input('Введите число:'))

    for i in range(1, number+1):
        print(f'{i}! = {fact(i)}')


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def task2():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} | {int(not (x and y) or z)}')


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки
# встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def task3():
    substring = input('First string : ')
    phrase = input('Second string: ')
    length_substr = len(substring)
    length_phrase = len(phrase)
    for i in range(length_substr):
        count = 0
        for j in range(length_phrase):
            if substring[i] == phrase[j]:
                count += 1
        print(f'{substring[i]} - {count}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def task4():
    length = int(input('Введите число: '))
    length = abs(length)
    numbers = []
    for num in range(-length, length+1):
        numbers.append(num)
    print(numbers)

    step = int(input('Введите сдвиг: '))
    result = numbers[-step:] + [numbers[:-step]]
    print(result)
task4()