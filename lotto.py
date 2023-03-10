import random

class Lotto:
    def __init__(self):
        self.moje_liczby = [5,7,14,23,34,39]

    def los(self):
        self.losy = [random.randint(1, 49) for element in range(6)]
        self.trafione = [element for element in self.moje_liczby if element in self.losy]
        return self.trafione


class Licznik:
    def __init__(self):
        self.budzet = 0
        self.wygrana = 0
        self.trafienia = {0:0, 1:0, 2:0, 3:24, 4:204.9, 5:5997.5, 6:4059640}

    def licz(self, punkty):
        self.budzet += -3
        self.wygrana += self.trafienia[punkty]
        self.wygrana = round(self.wygrana, 2)
        return f'    Wygrano Łącznie: {self.wygrana}zł     Przeznaczono na Zakłady: {self.budzet}zł'


class Jedziemy:
    def __init__(self):
        self.ilosc_prob = 0
        self.gra = Lotto()
        self.licznik = Licznik()

    def start(self):
        trafy = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        while len(self.gra.los()) != 6:
            trafy[len(self.gra.los())] += 1
            self.ilosc_prob += 1
            print(f'próba: {self.ilosc_prob}, {trafy}, {self.licznik.licz(len(self.gra.los()))}')
        trafy[6] += 1
        self.ilosc_prob += 1
        print(f'próba: {self.ilosc_prob}, {trafy}, {self.licznik.licz(6)}')
        print('MAMY 6!!!!')


Jedziemy().start()
