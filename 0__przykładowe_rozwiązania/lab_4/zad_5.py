
class Ciag:

    def __init__(self):
        self.start = None
        self.stop = None
        self.step = None
        self.ciag = []

    def wyswietl_dane(self):
        for elem in self.ciag:
            print(elem)

    def pobierz_elementy(self):
        while True:
            wejscie = input("Podaj liczbę lub wpisz 'koniec'\n")
            if wejscie != 'koniec':
                self.ciag.append(int(wejscie))
            else:
                break

    def pobierz_parametry(self):
        params = input("Podaj parametry oddzielone spacją: start stop step\n")
        param_list = [int(param) for param in params.split(" ")]
        self.start, self.stop, self.step = tuple(param_list)

    def policz_sume(self):
        return sum(self.ciag)

    def policz_elementy(self):
        # można tak, "na piechotę"
        # if self.start is not None and self.stop is not None and self.step is not None:
        # lub szybciej
        if None not in self.__dict__.values():
            self.ciag = [x for x in range(self.start, self.stop, self.step)]


if __name__ == "__main__":
    # przykładowe wykorzystanie klasy
    ciag = Ciag()
    ciag.wyswietl_dane()
    ciag.pobierz_parametry()
    ciag.policz_elementy()
    ciag.wyswietl_dane()