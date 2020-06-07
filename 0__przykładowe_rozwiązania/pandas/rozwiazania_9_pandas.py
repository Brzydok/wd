import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def zadanie1():
    xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    grouped = df.groupby('Rok').sum()
    grouped.plot()
    plt.ylabel('Liczba narodzonych dzieci')
    plt.show()


def zadanie2():
    xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    # w tym przypadku kolor słupków będzie taki sam
    grouped = df.groupby('Plec').agg({'Liczba':['sum']})
    grouped.plot.bar()
    plt.show()

    # żeby to zmienić trzeba rozdzielić dane, można to zrobić za pomocą funkcji unstack() lub poprzez pivot_table()
    grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
    grouped.plot.bar(color=['r','g'])
    plt.xlabel('Płeć')
    plt.show()

    # za pomocą pivot_table
    grouped = df.groupby('Plec').agg({'Liczba': [ 'sum' ]})
    table = pd.pivot_table(grouped, columns='Plec', values='Liczba', aggfunc=np.sum).plot.bar()
    plt.xlabel('Suma narodzin dzieci')
    plt.show()

def zadanie3():
    xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
    df = pd.read_excel(xlsx, 'Arkusz1')

    ostatnie_5_lat = df[(df.Rok > 2012)].groupby('Plec').agg({'Liczba':['sum']})
    ostatnie_5_lat.plot.pie(subplots=True, autopct='%.2f % %', fontsize=18)
    plt.show()


def zadanie4():
    df = pd.read_csv('iris.data', delimiter=',', header=None)
    # 0, 1, 2 to domyślne etykiety tego DataFrame, sprawdź wypisując df na konsolę
    wykres = df.plot.scatter(x=0, y=1, c=3, colormap='viridis')
    wykres.set_ylabel('sepal width')
    wykres.set_xlabel('sepal length')
    plt.show()


def zadanie5():
    df = pd.read_csv('zamowienia.csv', delimiter=';')
    policzone = df.groupby('Sprzedawca').size()
    policzone.plot.bar()
    plt.ylabel("liczba zamówień")
    plt.show()

    # można też dodać etykiety do słupków wykresu
    ax = policzone.plot.bar()
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.01, p.get_height() * 1.01))
    plt.ylabel("liczba zamówień")
    plt.show()


zadanie5()