# a = дописать в уже имеющийся файл
# если дописывать в НЕсуществующий ф-л, он будет создан и записан новой инф-ей

# r = читаем данные из файла
# чтение из НЕсуществующего ф-ла - будет ошибка

# w = (мод), создать файл + записать в него
#

# w+ открыть файл для записи + чтение из него
# r+  открыть  для чтения и дописыват в него

#===== вариант 1 (запись в файл )===========

# sport = ['sambo ', 'real_sport ', 'bjj'] # мои данные для записи в файл
# data = open('1sport.txt', 'a')   # ('откуда взять инф-ию', 'мод')
# #data.writelines(sport)           # writelines (запись в строку, без разделителей)
#
# data.write('\nJUDO\n')           # запись в файл идет прямо из аргумента
# data.write('\nbest fight\n')     # дозапись в файл идет прямо из аргумента
#
# data.close()                     # разрыв связи между 'sport' и '1sport.txt'

#===== вариант 2 (запись в файл ) ===========

with open('1sport-with.txt', 'a') as data:
    data.write('sambo\n')           # запись в файл идет прямо из аргумента
    data.write(' best sport\n')

#=====  (чтение файла ) ===========

path = '1sport-with.txt'
data = open(path, 'r')

for i in data:
    print(i)

data.close()


