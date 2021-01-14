'''Funkcje dotyczace dyskow na przestrzeni dwuwymiarowej (ich przesuwania i wykrywania kolizji).'''

import math


def kolizja(dysk1, dysk2):
    '''
    Funkcja wykrywa kolizje miedzy dwoma dyskami
    :param dysk1: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :param dysk2: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :return: True - dyski zachodza na siebie, False - nie zachodza
    '''
    if type(dysk1) == tuple and type(dysk2) == tuple and len(dysk1) == 3 and len(dysk2) == 3:
        odleglosc = math.sqrt((dysk2[0]-dysk1[0])**2 + (dysk2[1] - dysk1[1])**2)
        if odleglosc < (dysk1[2] + dysk2[2]):
            return True
        else:
            return False
    else:
        return 'Błędne dane'


def przesuniecie(dysk, wektor):
    '''
    Funkcja przesuwa dysk o podany wektor
    :param dysk: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :param wektor: krotka skladajaca sie z 3 liczb, 2 pierwsze to wspolrzedne srodka a 3 to promien
    :return: nowe wspolrzedne dysku
    '''
    if type(dysk) == tuple and type(wektor) == tuple and len(dysk) == 3 and len(wektor) == 2:
        nowy_dysk = (dysk[0] + wektor[0], dysk[1] + wektor[1], dysk[2])
        return nowy_dysk
    else:
        return 'Błędne dane'

