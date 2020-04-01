# Wizualizacja danych
## Lab 4. Operacje na plikach. Wstęp do programowania obiektowego.

### **1. Operacje na plikach**

Operacje na plikach można podzielić na 3 etapy:
1. Otwarcie pliku
2. Działanie na pliku (odczyt lub zapis)
3. Zamknięcie pliku.

```python
plik = open(nazwa, [tryb[, bufor]])
```

gdzie:

plik – nazwa obiektu, którą sami nadajemy  
nazwa – nazwa pliku na dysku, jaka jest  
tryb – tryb otwarcia pliku (np. do odczytu, do zapisu itd.)  
bufor – obszar pamięci przechowujący dane w oczekiwaniu na zapis i odczyt

Wybrane tryby otwarcia plików:  
| Tryb | Opis |
|------|------|
|r|Tylko do odczytu. Plik musi istnieć|
|w|Tylko do zapisu. Jeżeli pliku nie ma to zostanie utworzony a jeżeli jest to jego zawartość zostanie zapisana nową|
|a|Do dopisywania. Dane dopisuje się na koniec pliku. Jeśli plik nie istnieje to zostanie utworzony|
|r+|Do odczytu i zapisu. Plik musi istnieć.|
|w+|Do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony|
|a+|Do odczytu i zapisu. Jeżeli plik nie istnieje zostanie utworzony.|

Więcej opcji można znaleźć w oficjalnej dokumentacji:  
https://docs.python.org/3/library/functions.html?highlight=open#open


**Odczytanie danych z pliku:**

można użyć komend:
* read([rozmiar]) - odczytuje dane o rozmiarze, jeśli podany
* readline([rozmiar]) – odczytuje wiersz lub ilość znaków jeśli podano rozmiar
* readlines() – odczytuje wiersze z pliku

**Przykład 1**
```python
plik = open("Ćw1_przyklad1.py","r")

#odczyt 10 znaków z pliku
znaki = plik.read(10)

#odczyt jednej lini z pliku
linia = plik.readline()

#odczyt wierszy z pliku
wiersze = plik.readlines()

#zamkniecie pliku
plik.close()
#drukujemy 10 znakow

print(znaki)
print("\n")
#drukujemy linię

print(linia)
print("\n")
#drukujemy cały plik

print(wiersze)
print("\n")
```

**Uwaga!**  
Jeśli otwieramy plik i odczytujemy z niego dane jak wyżej to wskaźnik aktualnej pozycji w pliku się przemieszcza. Dlatego w wyniku najpierw otrzymamy pierwsze 10 znaków, potem następne znaki z pozostałej linijki a na koniec resztę linijek tekstu z pliku.

**Uwaga 2!**  
Po zakończeniu działania skryptu wszystkie otwarte pliki zamykane są automatycznie.
Zapisywanie danych do pliku
Możemy wykorzystać instrukcje:
* write(łańcuch) – zapisuje dane ze zmiennej łańcuch
* writelines(lista) – zapisuje dane z listy

**Przykład 2**
```python
import sys


print("Podaj kierunek studiów, rok i specjalność")
# odczyt danych ze standadrdowego wejścia
dane = sys.stdin.readline()

# Otwieramy plik
plik = open("dane.txt","w+")

# Zpaisujemy do pliku
plik.write(dane)

# zamykamy plik
plik.close()

# tworzymy liste
lista = []
for x in range(1,6,1):
    lista += [x]

# otwieramy plik do dopisywania
plik=open("dane.txt","a+")

# zapisujemy
plik.writelines(str(lista))

# zamykamy
plik.close()
```

**Przykład 3**
```python
# pliki możemy otwierać do odczytu i zapisu za pomocą komendy with
# wówczas nie musimy się martwić o zamykanie pliku
# Pętla for pozwala na wyświetlenie pliku linijka po linijce
with open("dane.txt", "r") as plik:
    for linia in plik:
    print(linia, end="")
```

**Zad. 1**  
Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

**Zad. 2**   
Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.

**Zad. 3**  
Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

### **2. Programowanie obiektowe - wprowadzenie.**

**Programowanie obiektowe – podstawowe terminy**

Programowanie obiektowe wymaga zaprojektowania struktury opartej na danych i kodzie. Taka struktura nazywana jest klasą a każdy obiekt stworzony na podstawie tej klasy to instancja instancją (albo wystąpieniem) danej klasy. Dane powiązane z obiektem to będą atrybuty ( inaczej własności lub właściwości) a funkcje, które wykonują coś na obiekcie to metody.

**Enkapsulacja** 

Inaczej zwana hermetyzacją. Chodzi o to by tak zdefiniować klasę aby jej metody obsługiwały wszystkie właściwości obiektu i żeby żadna funkcja z zewnątrz nie mogła zmienić właściwości obiektu.

**Dziedziczenie**

Jeśli po utworzeniu klasy okaże się, że potrzebujemy podobnej. np. chcemy stworzyć szafę grającą, która dodatkowo odtwarza mp3 to możemy zastosować dziedziczenie. Wówczas nowa klasa otrzymuje wszystkie właściwości tej, po której dziedziczy. Oryginalną klasę nazywamy klasą bazową (inne nazwy to nadklasa lub superklasa) a nową klasą pochodną (lub podklasą).

**Deklaracja klasy**

Składnia:
```python 
class NazwaKlasy[(KlasaBazowa1, KlasaBazowa2, KlasaBazowa3)]:
    instrukcje1
    instrukcje2
    instrukcjeN
```

**Przykład 4**

Definicja pustej klasy i utworzenie obiektu
```python
class PierwszaKlasa:
    """Przykład klasy"""


obiekt = PierwszaKlasa()
print(obiekt)
```

**Przykład 5**

Dodajemy atrybut
```python
class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321


obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
```

**Przykład 6**

Dodajemy metodę
```python
class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321

    def pierwsza_metoda(z):
        return "Teraz działa pierwsza Metoda"


obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda())
```

**Przykład 7**

Dodajemy atrybut do instancji klasy
```python
class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321
    def pierwsza_metoda(z):
        return "Teraz działa pierwsza Metoda"


obiekt = PierwszaKlasa()
print(obiekt)

#drukujemy atrybut
print(obiekt.atrybut)

#drukujemy metodę
print(obiekt.pierwsza_metoda())

#dodajemy atrybut do istniejącego obiektu
obiekt.tekst = "la la la"
print(obiekt.tekst)

#ale go nie będzie w nowej instancji klasy
nowy_obiekt = PierwszaKlasa()
print(nowy_obiekt.tekst)
```

**Konstruktory**

Konstruktor to specjalna funkcja, która tworzy obiekt. Jeśli nie zdefiniujemy swojej to w Pythonie jest wywoływany konstruktor domyślny. W Pythonie konstruktor nie tworzy instancji klasy a nadaje wartości początkowe do obiektu.

**Przykład 8**

```python
class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        #deklarujemy atrybuty
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole_prostokata(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


# Tworzymy obiekt
kwadrat= Ksztalty(10,30)

# Sprawdzamy teraz jak działają metody które zwracają wartość
print(kwadrat.pole_prostokata())
print(kwadrat.obwod())

# sprawdzamy jak działają metody, które nie zwracają wartości
kwadrat.dodaj_opis("Kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.5)
print(kwadrat.x)
print(kwadrat.y)
```

**Uwaga 1:**  
Zgodnie z dokumentacją słowo kwalifikujące self jest używane bo taka jest konwencja i nie ma specjalnego technicznego znaczenia.

**Uwaga 2:**  
Niektóre funkcje można poprzedzić znakami __ i dla nas będą miały specjalne znaczenie. Konwencja mówi, że wtedy będą to zmienne lub funkcje prywatne czyli takie, które są widoczne tylko dla jednej klasy i nie mogą być modyfikowane przez funkcje i zmienne z innej klasy. W rzeczywistości jest to tylko umowa bo w Pythonie nie ma prywatnych zmiennych czy funkcji, wszystkie są publiczne.

**Przykład 9**
Do Uwaga2.
```python
class Ksztalty:
    # definicja zmiennej poprzedzonej __
    __jestem_prywatna__ = "xyz"

    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole_prostokata(self):
        return self.x*self.y

    def obwod(self):
        return 2*self.x + 2*self.y

    def dodaj_opis(self, text):
        self.opis = text
        def skalowanie(self, czynnik):
        self.x = self.x *czynnik
        self.x = self.y *czynnik

    #Jakaś funkcja
    def zmieniam_tekst(tekst):
        tekst += " to jest to ;)"
        return tekst


# Tworzymy obiekt
Kwadrat = Ksztalty(10,30)

# Sprawdzmy dostęp do zmiennej prywatnej
print(kwadrat.__jestem_prywatna__)

# a może uda nam się jeszcze zmienić wartość?
kwadrat.__jestem_prywatna__="na na na"
print(kwadrat.__jestem_prywatna__)

# spróbujmy czy nowa funkcja coś może zmienić
print(zmieniam_tekst(kwadrat.__jestem_prywatna__))
```

**Zad. 4**  

Stwórz klasę **NaZakupy**, która będzie przechowywać atrybuty: 
* nazwa_produktu, ilosc, jednostka_miary, cena_jed 
oraz metody:
* konstruktor – który nadaje wartości
* wyświetl_produkt() – drukuje informacje o produkcie na ekranie
* ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
* ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

**Zad. 5**

Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:

* wyświetl_dane – drukuje elementy na ekran
* pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
* pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
* policz_sume – liczy sume elementow
* policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana

Stwórz instancję klasy i sprawdź działanie wszystkich metod.

**Zad. 6**

Utwórz klasę **Slowa**, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
* sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
* sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
* sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
* wyświetl_wyrazy – wyświetla podane wyrazy

Stwórz instancję klasy i sprawdź działanie wszystkich metod.

**Zad. 7**

Stwórz klasę **Robaczek**, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
* konstruktor – który nadaje wartość dla x, y i krok
* idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
* idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
* idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
* idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
* pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka

Stwórz instancję klasy i sprawdź jak działają wszystkie metody

**Finalizer  to odpowiednik destruktora i niszczy instancje obiektu.**

```python
__del__(self)
```

Więcej można doczytac poid adresem: [link](https://docs.python.org/3/reference/datamodel.html#object.__del__)

**Zad. 8**

Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.