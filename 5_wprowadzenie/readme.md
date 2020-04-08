# Wizualizacja danych
## Lab 5. Programowanie obiektowe - dziedziczenie. Iteratory i generatory.

### **1. Dziedziczenie**

Mając klasę bazową możemy utworzyć klasę pochodną, która będzie dziedziczyć po klasie bazowej czyli będzie miała dostęp do atrybutów i metod z klasy bazowej. W klasie pochodnej można dodać nowe metody lub atrybuty.

**Przykład 1**
```python
class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole_prostokatu(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


# a teraz klasa która dziedziczy po klasie Ksztalty
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x

# i jeszcze klasa, która dziedziczy po klasie Kwadrat
# bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
#  _
# | |_
# |_ _| 
class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        return 8 * self.x

    def pole_prostokatu(self):
        return 3 * self.x * self.y

print("inicjujemy klasę Kwadrat")
figura = Kwadrat(5)

# sprawdzamy metody z klasy bazowej
print(figura.pole_prostokatu())

print(figura.obwod())

figura.dodaj_opis("Kwadrat")

print(figura.opis)

figura.skalowanie(0.3)

print(figura.obwod())

print("inicjujemy klasę KwadratowaLiteraL")
litera_l = KwadratowaLiteraL(5)

# sprawdzamy jakie możemy wywołać metody
print(litera_l.obwod())
print(litera_l.pole_prostokatu())
litera_l.dodaj_opis("Litera L")
print(litera_l.opis)
litera_l.skalowanie(0.5)
print(litera_l.obwod())
```

Widać, że niektóre metody deklarujemy ponownie w potomnej klasie i to te nowe metody będą wywołane. To oznacza, że metody o tych samych nazwach w klasach potomnych zostały przesłonięte.

**Zad. 1**

Stwórz 3 klasy: Material, Ubrania, Sweter. Klasa: Material

Atrybuty:  
* rodzaj,
* długość
* szerokość

Metody:  
* konstruktor
* wyświetl_nazwę

Klasa: Ubrania  

Atrybuty:  
* rozmiar
* kolor
* dla_kogo

Metody:
* wyświetl_dane – do wyświetlania informacji o ubraniu

klasa: Sweter  

Atrybuty:  
* rodzaj_swetra – np. Rozpinany, z golfem itd.

Metody:  
* wyświetl_dane

Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.


### **2. Przesłanianie metod.**

Przykład przesłaniania metody został przedstawiony w przykładzie 1, ale warto dodać, że możemy również przesłaniać metody i zmienne dziedziczone po superklasie bazowej object, czyli tej, po której dziedziczy każdy obiekt w Pythonie. Możemy np. przeciążyć metodę `__str__()`, która zwraca tekstową reprezentację obiektu i domyślnie wyświetla informację o typie obiektu oraz adresie zajmowanym w pamięci komputera.

```python
class Kwadrat(Ksztalty):

    	def __init__(self, x):
            self.x = x
            self.y = x

		def __str__(self):
			return 'Kwadrat o boku {}'.format(self.x)

kw = Kwadrat(5)
print(kw)
```
Na konsoli zostanie wypisany tekst:
Kwadrat o boku 5

**Zad. 2**

Przeciąż metodę ``__add__()`` dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat o nowym boku, będącym sumą boków dodawanych do siebie kwadratów.

**Zad. 3**

Poczytaj o metodach `__ge__, __gt__, __le__, __lt__,` przeciąż je i spróbuj wykorzystać w instrukcji warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.


### **3. Atrybuty globalne, 'pusta' klasa oraz ponownie zmienna 'prywatna'**

Nawiązując do wprowadzenia do programowania obiektowego w języku Python należy wspomnieć o możliwości stworzenia atrybutów współdzielonych przez wszystkie instancje danej klasy.

**Przykład:**
```python
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)
```

Na wyjściu otrzymamy:
    
`[]
[]
[1]
[1]`


**Zad. 4**

Korzystając z powyższego kodu stwórz kilka instancji klasy Point i spróbuj odwołać się do zmiennej counter z poziomu różnych instancji, porównując jej wartość dla każdej z nich oraz spróbuj zmienić jej wartość.

Ciekawostką jest to, że możemy stworzyć „pustą” klasę tylko po to, żeby przechować wartość wielu zmiennych w pojedynczej referencji, coś jak struktura w języku C.


**Przykład:**
```python
class Pracownik:
    pass

janek = Pracownik()
janek.imie = "Janek"
janek.nazwisko = "Kowalski"
janek.wiek = 30
```

Wracając do zmiennych prywatnych z zestawu 4 warto jeszcze wiedzieć o sposobie „dostania” się do tej zmiennej.

**Przykład:**
```python
class Pracownik:
    __prywatna = "tajne hasło"

    def __init__(self, imie):
        self.imie = imie

janek = Pracownik("Janek")
print(janek.__prywatna)    # to nie zadziała
print(janek._Pracownik__prywatna)   # ale to już tak
```

### **3. Konstruktor klasy bazowej i dziedziczenie wielokrotne.**


Poniższy przypadek pokazuje ponownie dziedziczenie jednokrotne po klasie bazowej, gdzie mamy 3 klasy:
```python
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())
```

Zwróć uwagę na konstruktor klasy `Pracownik`, który wywołuje konstruktor bazowej klasy `Osoba`. Natomiast w definicji klasy `Manadzer` konstruktora nie ma a mimo to jestem w stanie zainicjalizować obiekt tak jak obiekt `Pracownik`. 

**Zad. 5**  
Za pomocą funkcji `isinstance()` oraz `issubclass()` sprawdź wynik dla instancji obiektu `Pracownik` oraz `Menadzer` dla klas `Osoba, Pracownik i Manadzer`.



Zwróć uwagę na poniższy przykład dziedziczenia wielokrotnego i konstruktor.
```python
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:

    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
print(adrian.przedstaw_sie())
```


### **4. Iteratory i generatory.**

Rozpatrując poniższy fragment kodu:
```python
for element in range(1, 11):
    print(element)
```

wszystko raczej jest jasne. Ale skąd pętla for wie jak ma się uniwersalnie zachowywać dla różnych obiektów iterowalnego ? Cały mechanizm jest obsługiwany przez iteratory. W niewidoczny dla nas sposób pętle for wywołuje funkcję `iter()` na obiekcie kolekcji. Funkcja zwraca obiekt iteratora, który ma zdefiniowaną metodę `__next__()`, odpowiedzialną za zwracanie kolejnych elementów kolekcji. Kiedy nie ma już więcej elementów kolekcji zgłaszany jest wyjątek `StopIteration`, kończący działanie pętli for. Można wywołać funkcję `__next__()` iteratora za pomocą wbudowanej funkcji `next()`.

**Przykład:**
```python
imie = "Reks"
it = iter(imie)
print(it)
# na wyjściu: <str_iterator object at 0x0000000003807FD0>
next(it)
# 'R'
next(it)
# 'e'
next(it)
# 'k'
next(it)
# 's'
next(it)
# Traceback (most recent call last):
#  File "<input>", line 1, in <module>
# StopIteration
```

Przykład implementacji własnego iteratora.
```python
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

**Zad. 6**  
Przetestuj powyższy iterator na kilku różnych kolekcjach.

**Zad. 7**  
Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów przekazanej kolekcji.

**Zad. 8**  
Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego. Zaimplementuj sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora (sprawdź funkcję `isinstance()`).


Generatory są prostymi narzędziami do tworzenia iteratorów. Generatory piszemy jak standardowe funkcje, ale zamiast instrukcji return używamy `yield` kiedy chcemy zwrócić wartość. Za każdym razem kiedy funkcja `next()` jest wywoływana na generatorze wznawia on swoje działanie w momencie, w którym został przerwany . Poniżej przykład generatora, którego działanie jest podobne do iteratora zaprezentowanego w przykładzie.

**Przykład:**
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


gen = reverse("Feliks")
print(next(gen))
print("Marek")
print(next(gen))
```

Na wyjściu otrzymamy:

s  
Marek  
k

Podobny efekt możemy również osiągnąć poprzez wyrażenia generujące.

**Przykład:**
```python
# wyrażenia generujące
litery = (litera for litera in "Zdzisław")
print(litery)
print(next(litery))
```

Na wyjściu:  
<generator object <genexpr> at 0x0000000003E96B48>  
Z


**Zad. 9**  
Przepisz jeden z napisanych przez siebie iteratorów na generator.

**Zad. 10**  
Zaimportuj pakiet itertools i znajdź w jego dokumentacji sposób na wygenerowanie kombinacji 3 elementowych bez powtórzeń na zbiorze 10 elementowym.

**Zad. 11**  
Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.

**Zad. 12**  
Za pomocą wyrażenia generującego stwórz generator zwracający polskie nazwy miesięcy.