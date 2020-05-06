
def zad_1():

    liczby_podzielne_przez_cztery = [x for x in range(4, 121, 4)]
    # 1 zapisze tak jakbyśmy wywołali print(lista)
    with open("podzielne_przez_cztery.txt","w") as plik:
        plik.writelines(str(liczby_podzielne_przez_cztery))

    # 2 zapiszemy liczba po liczbe oddzielone spacją
    with open("podzielne_przez_cztery.txt","w") as plik:
        plik.write(" ".join(str(liczba) for liczba in liczby_podzielne_przez_cztery))

    # 3 zapisze liczby w kolumnie
    with open("podzielne_przez_cztery.txt","w") as plik:
        for liczba in liczby_podzielne_przez_cztery:
            plik.write(str(liczba) + "\n")


def zad_2():

    # 1 bez with
    plik = open("podzielne_przez_cztery.txt")
    print(plik.readlines())

    # 2 z with ale tu też niezbyt ładnie na wyjściu to wygląda
    with open("podzielne_przez_cztery.txt") as plik:
        print(plik.readlines())


    # 3 skoro to lista linii to możemy przez nią iterować
    # lepiej, ale jest za każdym razem pusta linia, zagadka do samodzielnego rozwiązania
    # patrz print z wydruku powyżej
    with open("podzielne_przez_cztery.txt") as plik:
        for linia in plik:
            print(linia)


def zad_3():
    # tutaj pamiętajmy jak działa tryb w+, r+ oraz a+
    with open("podzielne_przez_cztery.txt", "r+") as plik:
        plik.write("Gdzie się to zapisze ?")
        print(plik.readlines())

    # ano zapisało się, ale na końcu, bo najpierw był zapis i "kursor" po zapisaniu ustawiony
    # jest za ostatnim zapisanym znakiem, wiec read nic nie odczyta w tym momencie
    # ale ponowne przeczytanie pliku już wyświetli te informacje
    # najwygodniej zapisywać, zamykac plik i otwierać do odczytu
    with open("podzielne_przez_cztery.txt") as plik:
        print(plik.readlines())


zad_1()
zad_2()
zad_3()
