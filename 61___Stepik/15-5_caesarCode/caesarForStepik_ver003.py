# This Python file uses the following encoding: utf-8
import os, sys
import re

#print('Шифр Цезаря')

# 1. Определение языка (в переменной lng)
def languae(text):

    countEn = 0
    countRu = 0

    for i in text:

        if 32<=ord(i)<=122:
            countEn +=1
            if countEn == len(text):
                lang = 'en'
                #print('Язык - английский (En)')
                #power = 26
                break

        if 32 <= ord(i) <= 64 or 1040 <= ord(i) <= 1103:
            countRu += 1
            if countRu == len(text):
                lang = 'ru'
                #print('Язык - русский (Ru)')
                # power = 32
                break

    else:
        #print('введено слово: Ru + En Выход из программы')
        exit()

    return lang


# 2. Со списком(массивом) какого языка будем работать
def baseAlphabet(lang):
    ru = ['абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 32]
    en = ['abcdefghijklmnopqrstuvwxyz' , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26 ]

    if lang == 'ru':
        return ru
    if lang == 'en':
        return en

#3. Найти длину каждого слова без учета спец.символов (нужно  для динамич. шифрования)
def getLength(text):

    arr = text.split(' ')
    arrLen = []

    for i in range( len(arr) ):
        arr[i] = re.sub(r'[,."!]', "" , arr[i])
        arrLen.append(len(arr[i]))

    #print(f' Длина каждого слова: {arrLen} ')
    return arrLen


# 4. ДЕШИФРУЕМ: decrypt()
# def decrypt(text, alphArr, length):
#
#     low, upp, power = alphArr
#     #print(low, upp, power )
#
#     step = int(input('Шаг сдвига(дешифруем: влево) >>> '))
#
#     newTxt = ''
#
#     for i in range(len(text)):
#
#         if text[i].isalpha():
#             if text[i].islower():
#                 print(f'\n{text[i]}, индекс: {i} --> (True) мал.буква до сдвига')
#                 lowIdx = str(low).find(text[i])
#                 print(f' в малом алфавите индекс буквы {text[i]}: {lowIdx}')
#                 lowEl = ( low[(lowIdx- step) % power])
#                 print(f'буква после сдвига влево: {lowEl}')
#                 newTxt +=lowEl
#
#             elif text[i].isupper():
#                 print(f'\n{text[i]}, индекс: {i} --> (True) бол.буква до сдвига')
#                 uppIdx = str(upp).find(text[i])
#                 print(f' в Большом алфавите индекс буквы {text[i]}: {uppIdx}')
#                 uppEl = (upp[(uppIdx - step) % power])
#                 print(f'буква после сдвига влево: {uppEl}')
#                 newTxt += uppEl
#
#         else:
#             newTxt += text[i]
#
#     print(newTxt)


# 4.1. ШИФРУЕМ: crypt()
def crypt(text, alphArr, length):

    low, upp, power = alphArr
    # print(low, upp, power )

    #print(f' Длина каждого слова: {length} ')

    #step = int(input('Шаг сдвига(шифруем: вправо) >>> '))
    stpEl = 0
    step = length[ stpEl]

    newTxt = ''

    for i in range(len(text)):

        if text[i].isspace():
            stpEl +=1
            step = length[stpEl]
            #print(f'замечен ПРОБЕЛ: теперь шаг = {step}')

        if text[i].isalpha():
            if text[i].islower():
                #print(f'\n{text[i]}, индекс: {i} --> (True) мал.буква до сдвига')
                lowIdx = str(low).find(text[i])
                #print(f' в малом алфавите индекс буквы {text[i]}: {lowIdx}')
                lowEl = (low[(lowIdx + step) % power])
                #print(f'буква после сдвига вправо: {lowEl}')
                newTxt += lowEl

            elif text[i].isupper():
                #print(f'\n{text[i]}, индекс: {i} --> (True) бол.буква до сдвига')
                uppIdx = str(upp).find(text[i])
                #print(f' в Большом алфавите индекс буквы {text[i]}: {uppIdx}')
                uppEl = (upp[(uppIdx + step) % power])
                #print(f'буква после сдвига вправо: {uppEl}')
                newTxt += uppEl

        else:
            newTxt += text[i]


    print(newTxt)





# 0. Старт: ввод текста
text = input()

# 1. Определение языка (в переменной lng), через lang возвращ. ru / en
lang = languae(text)

# 2. Алфавитная база (Ru or En), через base возвр. cписок [алфавит, АЛФАВИТ]
alphArr = baseAlphabet(lang)

# 3. Найти длину каждого слова (для динамическ. шифрования слов по их длине)
length = getLength(text)

#4. Что делаем - ДЕШИФРУЕМ: decrypt()  или ШИФРУЕМ: crypt()
# dataCode = input('1 - ДЕшифруем текст, 2 -  Шифруем текст >>>  ')
# if dataCode == '1':
#     decrypt(text, alphArr, length)
# if dataCode == '2':
crypt(text, alphArr, length)











