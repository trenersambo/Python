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


# 2. Со списком(массивом) какого языка будем работать
def baseAlphabet(lang):
    ru = ['абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
    en = ['abcdefghijklmnopqrstuvwxyz' , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    if lang == 'ru':
        return ru
    if lang == 'en':
        return en

# 3. ДЕШИФРУЕМ: decrypt()
def decrypt(text, alphArr):

    step = int(print('Шаг сдвига(вправо) >>> '))

    newTxt = ''

    for i in text:
        if i.isalpha()



# 3.1. ШИФРУЕМ: crypt()
def crypt(text, alphArr):
    pass
    #print('Шифруем', text, alphArr)

    #step = int(print('Шаг сдвига(вправо) >>> '))





# 0. Старт: ввод текста
text = input('введи текст тут >>> ')

# 1. Определение языка (в переменной lng), через lang возвращ. ru / en
lang = languae(text)

# 2. Алфавитная база (Ru or En), через base возвр. cписок [алфавит, АЛФАВИТ]
alphArr = baseAlphabet(lang)

#3. Что делаем - ДЕШИФРУЕМ: decrypt()  или ШИФРУЕМ: crypt()
dataCode = input('1 - ДЕшифруем текст, 2 -  Шифруем текст >>>  ')
if dataCode == '1':
    decrypt(text, alphArr)
if dataCode == '2':
    crypt(text, alphArr)










