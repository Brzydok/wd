# . - bieżący folder
# .. - folder nadrzędny

# cd ../../
# cd c:\windows\system32
# cd /usr/bin
# cd ../folder

# import os.path

# plik = open(r'c:\users\test\plik.txt')
# zdanie = 'Ostatnio czytałem \'Władcę Pierścieni\''
# zdanie = 'Ostatnio czytałem "Władcę Pierścieni"'
# r = raw

# w+	Do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony

# read() -> pusty string
# write('linia w pliku')
# read() -> pusty string

# linia w pliku

# plik.seek(0, 0)
# readline() -> string 'linia w pliku'

# liczba = 5
# imie = 'Zenon'
# print(type(liczba))
# print(type(imie))

# <class 'int'>
# <class 'str'>


# imie = 'Ala'
# # imie2 = imie
# print(id(imie))
# # print(id(imie2))
# imie = [z for z in range(1, 1000)]
# print(id(imie))

import numpy as np

mat = np.arange(25)
# teraz zmienimy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])  # od drugiego wiersza
print(mat[:, 1])  # druga kolumna jako wektor
print(mat[..., 1])  # to samo z wykorzystaniem ellipsis (...)
print(mat[:, 1:2])  # druga kolumna jako ndarray
print(mat[:, -1:])  # ostatnia kolumna
print(mat[1:3, 2:4])  # 2 i 3 kolumna dla 3 i 5 wierszu
print(mat[:, range(2,6,2)])  # 3 i 5 kolumna

