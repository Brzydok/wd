# Wizualizacja danych
## Lab 12. Scraping stron WWW.

## **1. Wprowadzenie do XPath**

XPath (ang. XML Path Language) pozwala na poruszanie się po strukturze dokumentu XML (HTML również) poprzez określanie odpowiednich selektorów.
Elementy, które możemy wskazywać i pobierać za pomocą XPath nazywane są węzłami. Węzły mogą być:
* węzłem głównym – root element
* węzłem elementu – element node
* węzłem atrybutu – attribute node
* wartości atomowe – atomic values – elementy, które nie mają rodzica lub potomków (np. wartości atrybutu lub tekst między tagami).

Rozpatrzmy poniższą strukturę dokumentu xml:
**Przykład 1**  
```xml
<?xml version="1.0" encoding="UTF-8"?>

<ksiegarnia>
  <ksiazka>
    <tytul lang="en">Władca Pierścieni</tytul>
    <autor>J.R.R. Tolkien</autor>
    <rok>1948</rok>
    <cena>99.99</cena>
  </ksiazka>
</ksiegarnia>
```

Element:
* `<ksiegarnia>` to węzeł główny,
* `<autor>J K. Rowling</autor>` to węzeł elementu,
* `lang="en"` to węzeł atrybutu.

Wartościami atomowymi (takimi, które nie mają rodzica ani potomka) są w tym przykładzie wartości `J.R.R. Tolkien` oraz `"en"`.

### **Relacje węzłów**

**Rodzic (ang. parent)**  
Każdy element może mieć jednego rodzica. W przykładzie 1 element `<ksiazka>` jest rodzicem dla elementów `<tytul>, <autor>, <rok>` oraz `<cena>`.

**Dzieci (ang. children)**  
Elementy mogą posiadać zero, jedno lub wiele dzieci. Wracając do przykładu 1 elementy `<tytul>, <autor>, <rok>` oraz `<cena>` są dziećmi elementu `<ksiazka>`.

**Rodzeństwo (ang. siblings)**  
Są to elementy, które posiadają tego samego rodzica. Ponownie nawiżaując do przykładu 1 rodzeństwem są elementy `<tytul>, <autor>, <rok>` oraz `<cena>` są rodzeństwem.

**Przodkowie (ang. ancestors)**  
Jest to rodzic węzła, rodzic rodzica, itd. W naszym przykładzie przodkami elementu `<tytul>` są elementy `<ksiazka>` oraz `<ksiegarnia>`.

**Potomkowie (ang. descendants)**  
Są to dzieci elementu, dzieci tych dzieci, itd. Potomkami elementu `<ksiegarnia>` są elementy `<ksiazka>`, `<tytul>, <autor>, <rok>` oraz `<cena>`.

### Pobieranie węzłów

|Wyrażenie|Opis|
|---|---|
nazwa_węzła | Pobiera wszystkie węzły o podanej nazwie
/ | Pobieranie elementów zostanie rozpoczęte od węzła głównego
// | Pobierane są węzły z całego dokumenty, które spełniają warunek po ukośnikach
. | Pobiera bieżący węzeł
.. | Pobiera rodzica bieżącego węzła
@ | Pobieranie atrybutów

Przykłady na podstawie naszego dokumentu xml.
|Ścieżka | Wynik
|---|---|
ksiegarnia | Pobiera wszystkie węzły z nazwą "księgarnia"
/ksiegarnia | Pobiera główny element "ksiegarnia", jest to ścieżka bezwzględna
ksiegarnia/ksiazka | Pobiera wszystkie elementy `<ksiazka>`, które są dziećmi elementu `<ksiegarnia>` 
//ksiazka | Pobiera wszystkie elementy `<ksiazka>` bez względu na to gdzie znajdują się w dokumencie
ksiegarnia//ksiazka | 	Pobierane są wszystkie elementy `<ksiazka>`, które są potomkami elementu `<ksiegarnia>` bez względu na zagnieżdżenie względem elementu `<ksiegarnia>`
//@lang | Pobiera wszystkie atrybuty o nazwie "lang"

To tylko wstęp i w zupełności nie wyczerpuje wiedzy na temat XPath, która warto posiąść. Po więcej informacji odsyłam do dokumentacji, na początek tej wylistowanej poniżej.

* https://www.w3schools.com/xml/xpath_intro.asp
* http://zvon.org/xxl/XPathTutorial/Output_pol/examples.html
* https://developer.mozilla.org/en-US/docs/Web/XPath



## **2. Pakiet lxml**

**Instalacja**  
Instalujemy pakiet `lxml` oraz `requests`.

**Pobierania zawartości strony**

Spróbujmy ściągnąć stronę listingu z BoardGameGeek i wyświetlić w konsoli źródło strony.

**Przykład 1:**  
```python
import requests

url = "https://boardgamegeek.com"
data = requests.get(url)
# print html
print(data.text)
```

**Parsowanie HTML**  

**Przykład 2:**  
```python
from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
# print html
print(data.text)

page = html.fromstring(data.text)
```

**Pobieranie informacji o elemencie**  
**Przykład 3:**  
```python
from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

# pobieramy wszystkie elementy typu <a> gdzie przodkiem jest <H2> oraz elementem nadrzędnym element o
# klasie "geekcentral_leftcol"
xpath = '//*[@class="geekcentral_leftcol"]//h2//a'

# iterowanie przez odnalezione elementy i wyświetlenie nazw i wartości atrybutów
foundElements = page.xpath(xpath)
for element in foundElements :
   print(element.tag, element.keys())
   for name, value in sorted(element.items()):
       print('%s = %r' % (name, value))
```

Poniższy przykład obrazuje możliwy proces pobrania danych tabelarycznych. Dokumenty HTML mogą być bardzo różnorodne i ze względu na czasem dość dowolną interpretację semantyki możliwe są bardzo różne kombinacje znaczników co wymusza indywidualne podejście do parsowania każdego nowego dokumentu.

**Przykład 4:**  
```python
from lxml import html
import requests

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)
#print html
# print(data.text)

page = html.fromstring(data.text)
# tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
# można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
table_div = page.get_element_by_id('collection')

# w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej 
# należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]
print(table)

# wyświetlamy wszystkie nagłówki tabeli (po przeanalizowaniu dokumentu okazało się, że nie użyto znacznika <thead> do oddzielenia nagłówka tabeli, szukamy więc tylko znaczników <th>)
labels = [label.strip() for label in table.xpath('.//th/text()')]
print(labels)

# kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
headers = [label for label in table.xpath('.//th')]
labels = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        labels.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        labels.append(header.text.strip())
print(labels)
```

**Zadanie 1**  
Ze strony https://boardgamegeek.com pobierz linki (znajdź odpowiednie atrybuty) z sekcji 'Announcements'. Wyświetl te linki.

**Zadanie 2**  
Korzystając z kodu z przykładu 4 dodaj kod, który pobierze wszystkie dane z tabeli, z której pobrane zostały nagłówki. Dane następnie zapisz do pandas DataFrame ale wyeliminuj kolumnę, w której jest obraz przedstawiający daną grę oraz kolumnę 'Shop'. Można to zrobić przed wstawieniem danych do frame'a.

**Zadanie 3**  
Z DataFrame'a uzyskanego w zadaniu 2 wyświetl 10 rekordów z największymi wartościami w kolumnie 'Num Voters'. Wyświetl również wykres słupkowy dla tych danych.


## Pakiet BeautifulSoup

Jest to jeden z bardziej znanych i rozbudowanych pakietów do web scrappingu dla języka Python.

Pakiet instalujemy poprzez `pip install beautifulsoup4`. Jeżeli pakiet `urllib3` nie jest zainstalowany (`pip list`) to również należy go zainstalować.

**Przykład 5:**  
```python
from bs4 import BeautifulSoup
import urllib3


url = "https://boardgamegeek.com/"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
print(page.data)
soup = BeautifulSoup(page.data, 'lxml')
# zawartość strony jest sformatowana w bardziej przystepny sposób, tak jakbyśmy przeglądali źródło strony w narzędziach developerskich przeglądarki
print(soup)
```

Pobranie zawartości tabeli może wyglądać jak poniżej.
**Przykład 6:**  
```python
from bs4 import BeautifulSoup
import urllib3


url = "https://boardgamegeek.com/browse/boardgame"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
print(page.data)
soup = BeautifulSoup(page.data, 'lxml')

for tr in soup.find('table').find_all('tr'):
    for td in tr.find_all('td'):
        # jeżeli obiekt/-y nie zostaną odnalezione to zwracany jest obiekt None
        if td.find('a'):
            print(td.find('a').text.strip(), end=' ')
            # w strukturze tabeli rok wydania gry w oddzielnym elemencie <span>
            if td.find('span'):
                print(td.find('span').text.strip(), end=' ')
        else:
            print(td.text.strip(), end=' ')
    print()
```

**Zadanie 4**  

Ze strony https://metacritics.com pobierz dane (tytuł, platforma, data wydania, ocena) z pierwszej strony wyników najbardziej popularnych gier video w kategorii 'strategy'. Zapisz dane do pandas DataFrame i je wyświetl.

**Zadanie 5**  

Do danych z zadania 4 dodaj dane z tej samej kategorii, ale z 10 pierwszych stron wyników i umieść wszystko w jednym DataFrame. Wyświetl 10 najlepiej ocenianych gier na platformę PC.

## Inne pakiety warte uwagi

Przeglądanie struktury dokumentu i nastepnie pobieranie danych jest dość żmudnym zajęciem, ale czasem nie ma innej drogi. Dużo łatwiej jest korzystać z API, które zostało udostępnione na zewnątrz (często odpłatnie). Jednak to nie jest sytuacja częsta dla mało popularnych danych lub stron, nad którymi nie mamy kontroli i nie możemy samodzielnie stworzyć stosownego mechanizmu. Czasem dużo łatwiej jest wyświetlić jakieś dane poprze operacje myszą/klawiaturą szczególnie dzisiaj, kiedy strony przepełnione są kodem JavaScript. Narzędziem, które jest niezwykle popularne, szczególnie jeżeli chodzi o testowanie aplikacji webowych, jest **Selenium**, dzieki któremu możemy symulować zdarzenia na stronie taj jakbyśmy byli użytkownikiem-człowiekiem.  
Innym pakietem, którego użycie w procesie web scrappingu są PyQuery oraz popularny ostatnio **Scrappy**.

Więcej info na stronie https://elitedatascience.com/python-web-scraping-libraries

