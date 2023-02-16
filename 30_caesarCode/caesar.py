# This Python file uses the following encoding: utf-8
import os, sys

print('Шифр Цезаря')

# 1. Определение языка (в переменной lng)
def languae(text):

    countEn = 0
    countRu = 0

    for i in text:

        if 32<=ord(i)<=122:
            countEn +=1
            if countEn == len(text):
                lang = 'en'
                print('Язык - английский (En)')
                #power = 26
                break

        if 32 <= ord(i) <= 64 or 1040 <= ord(i) <= 1103:
            countRu += 1
            if countRu == len(text):
                lang = 'ru'
                print('Язык - русский (Ru)')
                # power = 32
                break

    else:
        print('введено слово: Ru + En Выход из программы')
        exit()

    return lang


# Со списком(массивом) какого языка будем работать
def baseAlphabet(lang):
    ru = ['абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
    en = ['abcdefghijklmnopqrstuvwxyz' , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    if lang == 'ru':
        return ru
    if lang == 'en':
        return en





    # code = input('\nДля шифрования введи 1\n'
    #             'Для дешифровки введи 2\n >> ввод >>  ')

    # step = input('\nУкажи шаг сдвига (вправо)\n'
    #              '>> ввод >>  ')




# 0. Старт: ввод текста
text = input('введи текст тут >>> ')

# 1. Определение языка (в переменной lng), через lang возвращ. ru / en
lang = languae(text)

# 2. Алфавитная база (Ru or En), через base возвр. cписок [алфавит, АЛФАВИТ]
alphArr = baseAlphabet(lang)

#3. Что делаем - ШИФРУЕМ: decrypt()  или ДЕШИФРУЕМ: crypt()
dataCode = input('1 - ДЕшифруем текст, 2 -  Шифруем текст >>>  ')
if dataCode == '1':
    (text, alphArr)
if dataCode == '2':
    crypt(text, alphArr)











