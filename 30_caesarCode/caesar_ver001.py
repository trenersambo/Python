# This Python file uses the following encoding: utf-8
import os, sys

print('Шифр Цезаря')

def inMenu():
    code = input('\nДля шифрования введи 1\n'
                'Для дешифровки введи 2\n >> ввод >>  ')

    alph = input('\nУкажи алфавит\n'
                 'Если русский - введи 1\n'
                 'Если английский - введи 2\n >> ввод >>  ')
    step = input('\nУкажи шаг сдвига (вправо)\n'
                 '>> ввод >>  ')
    text = input('Текст для работы >>> ')

    return code, alph, step, text


def alphabet(code, alph, step, text):
    low_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upp_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    low_en = 'abcdefghijklmnopqrstuvwxyz'
    upp_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    alph = '0'

    while alph == '0':
        if alph == '1' and (text in low_ru or text in upp_ru):
            low = low_ru
            upp = upp_ru
            power = 32
        if alph == '2' and (text in low_en or text in upp_en):
            low = low_en
            upp = upp_en
            power = 26
        print('Код языка НЕ соответствует введенному тексту')

    return low, upp, power



def test(code, alph, step, text):
    print(f'\n ')
    print(f'Рабочий текст: {text}')
    if alph == '1':
        print('код 1: Русский (ru)')
    else:
        print('код 2: Английский (en)')
    if code == '1':
        print('код 1: Шифруем ')
    else:
        print('код 2: Расшифровываем ')
    if step:
        print(f'шаг сдвига = {step}')






def caesar(code, alph, step, text, low, upp, power):
    print(code, alph, step, text,low, upp, power)





# Блок вызова ф-ций
menu = inMenu()
low_upp = alphabet(*menu)
test(*menu)

caesar(*menu, *low_upp)






