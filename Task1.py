#  Задача 1. Напишите программу, которая принимает на вход число N и выдает список
#  факториалов для чисел от 1 до N.

def fact(number):
    res = 1
    for i in range(1, number+1):
        res *= i
    return res


def task1():
    number = int(input('Введите число: '))

    for i in range(1, number+1):
        print(f'{i}! = {fact(i)}')


# 
