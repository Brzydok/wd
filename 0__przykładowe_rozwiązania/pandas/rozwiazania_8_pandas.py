import pandas as pd
import numpy as np
import xlrd
import openpyxl


xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
df = pd.read_excel(xlsx,'Arkusz1')
# print(df.head())

def zadanie2_1():
    print(df[df['Liczba']>1000])


def zadanie2_2():
    print(df[df['Imie'] == 'KRZYSZTOF'])


def zadanie2_3():
    print(df.agg({'Liczba':['sum']}))


def zadanie2_4():
    print(df[((df['Rok'] >= 2000) & (df['Rok'] <= 2005))].agg({'Liczba':['sum']}))


def zadanie2_5():
    print(df.groupby(['Plec']).agg({'Liczba':['sum']}))


def zadanie2_6():
    # # funkcja nth zwraca n-ty wiersz każdej grupy lub listę wierszy jeżeli n jest listą liczb całkowitych
    # # pierwszy wiersz każdej grupy, możemy grupować po wielu kolumnach jednocześnie, jak w SQL
    # print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
    # # pierwsze 2 wiersze każdej grupy
    # print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth([0, 1]))
    # # lub w tym przypadku zadziała również funkcja first(), chociaż służy ona głównie do określania ilości wartości dla
    # # szeregów czasowych. Więcej pod adresem
    # # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.first.html
    # print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

    # alternatywne rozwiązanie
    new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
    for index, group in enumerate(new_df, start=1):
        print(f"{index} {group[0]}")
        print(f" {group[1].iloc[0]['Imie']}", end='')
        print(f" {group[1].iloc[0]['Liczba']}")

    # lub z trochę innym formatem
    prev_rok = 0
    for index, group in enumerate(new_df, start=1):
        rok = group[0][0]
        # plec = group[0][1]
        if rok != prev_rok:
            print(rok)
        prev_rok = rok
        # print(f"{plec}")
        print(f" {group[1].iloc[0]['Imie']}", end='')
        print(f" {group[1].iloc[0]['Liczba']}")
    # print(new_df)



def zadanie2_7():
    # dla chłopców i dziewczynek pogrupowane oddzielnie i pobrany pierwszy element (czyli o indeksie 0)
    # dane są posortowane, co pozwala na zwrócenie min lub max wartości danej ramki danych
    print("Chłopiec")
    print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),
                                                                                      ascending=False).iloc[0])
    print("Dziewczynka")
    print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                       ascending=False).iloc[0])
    # tym razem za pomocą jednej operacji, ale grupowania po dwóch kolumnach,
    # zwracamy 2 pierwsze wiersze (indeksy 0 oraz 1)
    print(df.groupby(['Plec', 'Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[[0,1]])
    # poniżej zwrócenie największej wartości dla wyniku, bez sortowania
    print("max")
    print(df.groupby(['Plec', 'Imie']).agg({'Liczba':['sum']}).max())


# zadanie2_1()
# zadanie2_2()
# zadanie2_3()
# zadanie2_4()
# zadanie2_5()
zadanie2_6()
# zadanie2_7()

df = pd.read_csv('zamowienia_ok.csv', delimiter=';')
# print(df)
# print(df.dtypes)

def zadanie3_1():
    # funkcja unique() zwraca unikalną LISTĘ wartości z podanej w tym przypadku kolumny 'Sprzedawca'
    print(df['Sprzedawca'].unique())
    # można również to osiągnąć korzystając z poznanych w pierwszych częściach technik
    # np. rzutowania listy na zbiór (set), który usuwa duplikaty
    # najpierw trzeba jednak w jakiś sposób wyciągnąć listę samych wartości w formie, która będzie bardziej "przystępna"
    # niż Pandas Series lub DataFrame
    # atrybut values zwraca listę wartości serii lub kolumny DataFrame, więc możemy ją rzutować na typ set()
    print(set(df['Sprzedawca'].values))
    # ale wcale nie musimy tego robić, bo rzutowanie Pandas Series na typ set() również przyniesie pożądany efekt
    print(set(df['Sprzedawca']))


def zadanie3_2():
    # jeżeli mamy zwrócić n największych wartości z danego zbioru (ale nie dla każdej grupy z funkcji groupby) wystarczy
    # dane odpowiednio posortować i pobrać odpowiedni wycinek
    # tutaj 5 pierwszych wierszy
    print(df.sort_values(by='Utarg', ascending=False)[0:5])
    # tu 5 pierwszych wartości z kolumny Utarg
    print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])
    # a tutaj to samo co przykład wyżej, ale jako Numpy array a nie DataFrame
    print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5].values)


def zadanie3_3():
    # funkcja size zwróci liczebność każdej z grup
    print(df.groupby(['Sprzedawca']).size())
    # count działa podobnie, ale zlicza ilość elementów, które nie są NaN w każdym wierszu lub kolumnie
    print(df.groupby(['Sprzedawca']).count())
    # łączna liczba zamówień dla sprawdzenia poprawności
    print(df.groupby(['Sprzedawca']).size().sum())


def zadanie3_4():
    print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))


def zadanie3_5():
    print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') &
              (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))


def zadanie3_6():
    # możemy również oprócz zwracania określonej liczby wierszy Series lub DataFrame zwrócić określony fragment samego
    # wiersza, np. stringa. Tutaj dla każdego wiersze z kolumny 'Data zamowienia' zwracane są 4 pierwsze znaki czyli
    # wartość roku
    print(df['Data zamowienia'].str[:4])
    # tutaj tej samej techniki używamy do pogrupowania danych po roku (4-ech pierwszych znakach kolumny)
    print(df.groupby(df['Data zamowienia'].str[:4]).agg({'Utarg':['mean']}))
    # tutaj wybieramy tylko określnone rekordy, gdzie pierwsze 4 znaki są równe 2004 i liczymy średnią
    print(df[((df['Data zamowienia'].str[:4] == '2004'))].agg({'Utarg': ['mean']}))
    # lub za pomocą funkcji mean()
    print(df[((df['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())


def zadanie3_7():
    # stosując tę samą technikę filtrujemy dane dla wyznaczonych lat
    rok_2004 = df[((df['Data zamowienia'].str[:4] == '2004'))]
    rok_2005 = df[((df[ 'Data zamowienia'].str[ :4 ] == '2005')) ]
    # można to oczywiście zrobić bardziej "klasycznie"
    rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
    # zapisujemy dane do plików
    rok_2004.to_csv("zamowienia_2004.csv", index=False)
    rok_2005.to_csv("zamowienia_2005.csv", sep=';', index=False)



# zadanie3_1()
# zadanie3_2()
# zadanie3_3()
# zadanie3_4()
# zadanie3_5()
# zadanie3_6()
# zadanie3_7()

# przykład jak można sobie poradzić z "niedoskonałymi" plikami danych

# po pierwsze, pliki można wczytywać z różnym kodowaniem
# wcześniej kodowanie możemy sprawdzić korzystając z poznanych wcześniej sposobów obsługi plików
# df = pd.read_csv('zamowienia.csv', encoding='utf8')
file = open('zamowienia.csv')
print(file.encoding)
file.close()
# df = pd.read_csv('zamowienia.csv', encoding=file.encoding)
# jeżeli to nie zadziała to możemy dodać jeszcze parametr, który zignoruje błędy
file = open('zamowienia.csv', errors='ignore')

df = pd.read_csv(file, delimiter=';')
file.close()
print(df)
# skoro mamy już dane w DataFrame możemy poddać je dalszej obróbce
# dane w kolumnie Utarg nie wyglądają tak jak powinny. Mianowicie separatorem powinna być kropka oraz
# powinniśmy się pozbyć literki n na końcu
# tutaj możemy skorzystać ze sposobów poznanych w pierwszej części semestru
# 1. ucinamy 2 ostatnie znaki ciągu tekstowego
# 2. zamieniamy przecinek na kropkę
# 3. zamieniamy spację na "brak spacji"
# 4. zmieniamy typ kolumny
df['Utarg'] = df['Utarg'].str[:-2].str.replace(',', '.').str.replace(' ','').astype('float64')
print(df)
print(df.dtypes)
df['Utarg'].apply(lambda x: x*2)
print(df)
df.to_clipboard()