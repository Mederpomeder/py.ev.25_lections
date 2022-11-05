#Работа с файлами

"""
каретка - указатель - курсор

open(<путь да файла>)
"""

# file = open('/home/meder/Desktop/ev.25/files/lections/files.py') # абсолютный путь 
# file = open('files.py') # относительный путь (относительно той директории, в которой вы работаете)

# Режимы работы с файлами
# 1. чтение -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавление -> a/a+ (append)
# b x t -> бинарное чтение

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r+')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(len(data))
# file.close()

# контекстный менеджер 

# with open('test.txt') as file:
#     print(file.tell())
#     data = file.read()
#     index = data.index('My')
#     print(file.tell())
#     file.seek(index)
#     print(file.tell())
#     print(file.read())
#     print(file.tell())
    
# file.tell() -> возвращает индекс, где находится указатель(курсор/указатель)
# file.seek(index) -> перемещает каретку на индекс, который вы передали

# with open('test.txt', 'r+') as file:
#     print(file.readlines())
#     file.seek(0)
#     print(file.readline())

# with open('test.txt', 'a+') as f:
#     f.write('\nHe is bastard of Ned Stark')
#     f.write('This is lesson about files!\n')
#     f.seek(0)
#     print(f.read())

# with open('test.txt', 'w+') as file:
#     file.write('Hello, file was opened with open!')

# def longest_words(filename):
#     with open(filename) as file:
#         words = file.read().split()
#     words.sort(key =len, reverse=True)
#     max_len = len(words[0])
#     res = []
#     for i in words:
#         if len(i) == max_len:
#             res.append(i)
#         else:
#             break
#         return res if len(res) > 1 else res.pop()

# print(longest_words('test.txt'))

# accounts = [[1,5],[7,3],[3,5]]

# print(max([sum(i) for i in accounts]))

# word = 'abcdefd' #->'dcbaefd'
# ch = 'd'

# def func(word, ch):
#     mid = word.index(ch)
#     s1 = word[0:mid+1]
#     s2 = word[mid+1:]
#     return s1[::-1]+s2
# print(func(word, ch))


# list_ = ['123', '12sd', '54', 'das', '142']
# def func(l):
    #res = list(map(lambda num: int(num) ,filter(lambda str_:str_.isdigit(), l)))
    #res = [int(i) for i in list_ if i.isdigit()]
    # res = []
    # for i in list_:
    #     if i.isdigit():
    #         res.append(int(i))
    # return res
# print(func(list_))

# list_ = ['123', '12sd', '54', 'das', '142']
# index = 2
# for i in range(len(list_)):
#     if i == index:
#         list_.pop()
# print(list_)

# a = {'a': 1, 'b': 34, 'c': None, 'd': 5, 'e': None}
# for i in a.copy():
#     if a[i] == None:
#         a.pop(i)
# print(a)



# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_codes(image):
#     string = pytesseract.image_to_string(image)
#     #print(string)
#     list_of_imei = re.findall(
#             r'IMEI\d.\s\d+', string)
            
#     print(list_of_imei)
    
#     with open('imei_codes.txt', 'w') as file:
#         for x in list_of_imei:
#             file.write(f'{x}\n')


# ls = 'imei.jpg'
# get_imei_codes(ls)


